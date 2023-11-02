import json
import re as regex
from controller import * 
import sqlite3 as ora
from Jugador import Jugador
from strings import ui_data_saved, ui_error, ui_save_csv


class Equipo:

    
    def __init__(self, archivo_json) -> None:
        """Contructor de Equipo

        Args:
            archivo_json (_type_): Recibe un archivo json con un formato especifico
        """
        json = self.load_json(archivo_json)
        self._equipo = json.get('equipo')
        self._jugador = [Jugador(jugador) for jugador in json.get('jugadores')]

    @property
    def equipo(self):
        return self._equipo

    @equipo.setter
    def equipo(self, value):
        self._equipo = value

    @property
    def jugador(self):
        return self._jugador

    @jugador.setter
    def jugador(self, value):
        self._jugador = value

    def listar_jugadores(self, max:int, contador:int) -> str:
        """Imprime todos los jugadores segun su indice de la lista"""
        for id, jugador in enumerate(self.jugador):
            if contador > id:
                print(f"""{jugador} PORCENTAJE: {(jugador.calcular_valor() * 100 / max):.0f}% | ROBOS: {jugador.stats.robos_totales} | BLOQUEOS: {jugador.stats.bloqueos_totales} | TOTAL: {jugador.calcular_valor()}""")

    def listar_jugadores_posicion(self) -> str:
        """Imprime todos los jugadores segun su posicion de juego y en el indice de la lista"""
        for id, jugador in enumerate(self.jugador):
            print(f"""{id}.-{jugador} - {jugador.posicion}""")

    def seleccionar_jugador(self, index:int) -> str:
        """Selecciona un jugador por indice

        Args:
            index (int): El index tiene que ser entero

        Returns:
            str: imprime nombre y estadisticas del jugador
        """
        if index > len(self.jugador):
            ui_error('Out-Of-Index')
            return False
        jugador = self.jugador[index]
        print(f'''{jugador.nombre}\n\n{jugador.stats}''')

    def buscar_jugador_por_nombre(self, nombre:str) -> str:
        """Busca un jugador por su nombre

        Args:
            nombre (str): espera un nombre de tipo string

        Returns:
            str: imprime jugador y sus logros, retorna True
        """
        for jugador in self.jugador:
            if regex.search(nombre, jugador.nombre, regex.IGNORECASE):
                print(f'\n{jugador}\n')
                jugador.jugador_logros()
                return(True)
        print('El jugador no existe')
    
    def mostrar_promedios(self) -> str:
        """Calcula promedios, lo imprime y ademas, muestra los promedios individuales de los jugadores

        Returns:
            str: devuelve el calculo de promedios
        """
        promedio = 0
        subtotal = 0
        orden = sorted(self.jugador, key=lambda p: p.nombre)
        for jugador in orden:
            subtotal += jugador.stats.promedio_puntos_por_partido
            promedio = f'El promedio final es de: {subtotal / (len(self.jugador) + 1):.2f}'
            print(f"{jugador.nombre}:\nPromedio de puntos por partida: {jugador.stats.promedio_puntos_por_partido}")
        print(promedio)

    def salon_de_la_fama(self, nombre:str) -> str:
        """Indica si el jugador pertenece al salon de la fama del baloncesto

        Args:
            nombre (str): Necesita un nombre de jugador

        Returns:
            str: Imprime si pertenece o no
        """
        for jugador in self.jugador:
            if regex.search(nombre, jugador.nombre, regex.IGNORECASE):
                if 'Miembro del Salon de la Fama del Baloncesto' in jugador.logros:
                    print(f'\n{jugador}\n')
                    print('Pertenece! Bien hecho!')
                    return(True)
        print('\nEl jugador no existe')

    def mayor_rebotes(self) -> str:
        """Indica cual es el jugador con mayor rebotes

        Returns:
            str: Imprime nombre y rebotes totales del jugador mas alto
        """
        flag = True
        j_nombre = 0
        j_rebotes = 0
        for jugador in self.jugador:
            if(flag):
                j_nombre = jugador.nombre
                j_rebotes = jugador.stats.rebotes_totales
                flag = False
            elif(j_rebotes <= jugador.stats.rebotes_totales):
                j_nombre = jugador.nombre
                j_rebotes = jugador.stats.rebotes_totales
        print(f'\nNombre del jugador es: {j_nombre},\nTotal de: {j_rebotes} rebotes')

    def ordenar_jugadores(self, orden:str):
        """Ordena los jugadores por temporadas con metodo de burbujeo

        Args:
            orden (str): Debemos indicar si el orden es Asc o Desc
        """
        n = len(self.jugador)
        jugador = self.jugador
        match orden:
            case 'Desc':
                for i in range(n):
                    for j in range(0, n-i-1):
                        if jugador[j].stats.temporadas < jugador[j+1].stats.temporadas:
                            jugador[j], jugador[j+1] = jugador[j+1], jugador[j]

                optional = str(input(ui_save_csv())).lower().capitalize()
                if(optional == 'Yes' or optional == 'Y'):
                    self.save_csv_MAXIMILIANO()

            case 'Asc':
                for i in range(n):
                    for j in range(0, n-i-1):
                        if jugador[j].stats.temporadas > jugador[j+1].stats.temporadas:
                            jugador[j], jugador[j+1] = jugador[j+1], jugador[j]

                optional = str(input(ui_save_csv())).lower().capitalize()
                if(optional == 'Yes' or optional == 'Y'):
                    self.save_csv_MAXIMILIANO()

            case _:
                print('Entrada no correcta, por favor escribir unicamente Desc/Asc')

    def load_json(self, archivo_json):
        """Se encarga de tomar el json y cargarlo
        Args: 
            archivo_json (str): Espera un archivo json con un formato especifico"""
        try:
            with open(archivo_json, 'r', encoding="utf-8") as json_file:
                data = json.load(json_file)
                return(data)
        except FileNotFoundError as file_error:
            print(f"""{file_error}\nNo se encontro el archivo""")

    def save_csv(self, valor:int) -> None:
        """Guarda los datos de un jugador en un archivo csv

        Args:
            valor (int): Espera un indice de jugador
        """
        try:
            jugador = self.jugador[valor]
            columnas = ('nombre, posicion, temporadas, puntos_totales, promedio_puntos_por_partido,\
                        rebotes_totales, promedio_rebotes_por_partido, asistencias_totales,\
                        promedio_asistencias_por_partido, robos_totales, bloqueos_totales,\
                        porcentaje_tiros_de_campo, porcentaje_tiros_libres, porcentaje_tiros_triples\n')
            with open(f'data/{jugador.nombre} - Stats.csv', mode='w') as file:
                file.write(columnas)
                file.write(f"{jugador.nombre},\
                            {jugador.posicion},\
                            {jugador.stats.temporadas},\
                            {jugador.stats.puntos_totales},\
                            {jugador.stats.promedio_puntos_por_partido},\
                            {jugador.stats.rebotes_totales},\
                            {jugador.stats.promedio_rebotes_por_partido},\
                            {jugador.stats.asistencias_totales},\
                            {jugador.stats.promedio_asistencias_por_partido},\
                            {jugador.stats.robos_totales},\
                            {jugador.stats.bloqueos_totales},\
                            {jugador.stats.porcentaje_tiros_de_campo},\
                            {jugador.stats.porcentaje_tiros_libres},\
                            {jugador.stats.porcentaje_tiros_triples}")
                print(ui_data_saved())
        except IndexError as error:
            print(ui_error(error))

    def save_csv_MAXIMILIANO(self):
        """Guarda nombre, posicion y estadisticas de un jugador en un archivo csv"""
        try:
            jugadores = self.jugador
            columnas = ('nombre, posicion, temporadas, puntos_totales, promedio_puntos_por_partido,\
                        rebotes_totales, promedio_rebotes_por_partido, asistencias_totales,\
                        promedio_asistencias_por_partido, robos_totales, bloqueos_totales,\
                        porcentaje_tiros_de_campo, porcentaje_tiros_libres, porcentaje_tiros_triples\n')
            with open('data/RIVERA_MENDES.csv', mode='w') as file:
                file.write(columnas)
                for jugador in jugadores:
                    file.write(f"{jugador.nombre},\
                                {jugador.posicion},\
                                {jugador.stats.temporadas},\
                                {jugador.stats.puntos_totales},\
                                {jugador.stats.promedio_puntos_por_partido},\
                                {jugador.stats.rebotes_totales},\
                                {jugador.stats.promedio_rebotes_por_partido},\
                                {jugador.stats.asistencias_totales},\
                                {jugador.stats.promedio_asistencias_por_partido},\
                                {jugador.stats.robos_totales},\
                                {jugador.stats.bloqueos_totales},\
                                {jugador.stats.porcentaje_tiros_de_campo},\
                                {jugador.stats.porcentaje_tiros_libres},\
                                {jugador.stats.porcentaje_tiros_triples}\n")
                print(ui_data_saved())
        except IndexError as error:
            print(ui_error(error))
        except IOError as error:
            print(ui_error(error))

    def save_json_MAXIMILIANO(self, nombre_archivo:str):
        """Guarda datos de jugadores en un archivo JSON

        Args:
            nombre_archivo (str): Debemos indicar con que nombre deseamos guardarlo
        """
        pattern = r'^[a-zA-Z-0-9]+$'
        datos = []
        for jugador in self.jugador:
            datos.append(jugador.convertir_diccionario())
        if regex.search(pattern, nombre_archivo.lower(), regex.IGNORECASE):
            with open(f'data/{nombre_archivo}.json', mode='w') as file:
                patron_json = {'equipo' : 'Dream Team','jugadores': datos}
                json.dump(patron_json, file, indent=4, ensure_ascii=False)
            file.close()
        self.save_to_database()

    def save_to_database(self):
        """Guarda la informacion de los jugadores en una base de datos"""
        try:
            jugadores = self.jugador
            createTable()
            for jugador in jugadores:
                instruccion = "INSERT INTO jugadores (nombre, posicion, temporadas) VALUES (?,?,?)"           #, posicion, estadisticas, logros, ?, ?, ?
                parametro = f'{jugador.nombre}, {jugador.posicion}, {jugador.stats.temporadas}'                                    #, jugador.posicion, null, test="".join(map(str,jugador.logros))
                insertRow(instruccion, parametro)
            print("Datos guardados correctamente.")
        except Exception as error:
            print("Ocurrió un error:", error)


    def orden_sumando_valores(self):
        n = len(self.jugador)
        jugador = self.jugador
        max_value = 0
        for i in range(n):
            for j in range(0, n-i-1):
                if jugador[j].calcular_valor() < jugador[j+1].calcular_valor():
                    jugador[j], jugador[j+1] = jugador[j+1], jugador[j]
        for jugador in jugador:
            flag = False
            if(flag):
                max_value = jugador.calcular_valor()
                flag = False
            elif(max_value < jugador.calcular_valor()):
                max_value = jugador.calcular_valor()
        try:
            contador = int(input('Por favor, indicar cuantos jugadores desea listar?\n')) 
            self.listar_jugadores(max_value, contador)
        except ValueError as error:
            ui_error(error)

            # ------------ EJEMPLO CON libreria CSV 
            # ------------ para funcionar requiere libreria CSV
        
            # columnas = ['nombre', 'posicion', 'temporadas', 'puntos_totales', 'promedio_puntos_por_partido',
            #             'rebotes_totales', 'promedio_rebotes_por_partido', 'asistencias_totales',
            #             'promedio_asistencias_por_partido', 'robos_totales', 'bloqueos_totales',
            #             'porcentaje_tiros_de_campo', 'porcentaje_tiros_libres', 'porcentaje_tiros_triples']
            # with open(f'data/{jugador.nombre} - Stats.csv', mode='w', newline="") as csv_file:
            #     escribir = excel.DictWriter(csv_file, fieldnames=columnas) 
            #     escribir.writeheader()
            #     escribir.writerow({'nombre': jugador.nombre,
            #                         'posicion': jugador.posicion,
            #                         'temporadas': jugador.stats.temporadas,
            #                         'puntos_totales': jugador.stats.puntos_totales,
            #                         'promedio_puntos_por_partido': jugador.stats.promedio_puntos_por_partido,
            #                         'rebotes_totales': jugador.stats.rebotes_totales,
            #                         'promedio_rebotes_por_partido': jugador.stats.promedio_rebotes_por_partido,
            #                         'asistencias_totales': jugador.stats.asistencias_totales,
            #                         'promedio_asistencias_por_partido': jugador.stats.promedio_asistencias_por_partido,
            #                         'robos_totales': jugador.stats.robos_totales,
            #                         'bloqueos_totales': jugador.stats.bloqueos_totales,
            #                         'porcentaje_tiros_de_campo': jugador.stats.porcentaje_tiros_de_campo,
            #                         'porcentaje_tiros_libres': jugador.stats.porcentaje_tiros_libres,
            #                         'porcentaje_tiros_triples': jugador.stats.porcentaje_tiros_triples})
