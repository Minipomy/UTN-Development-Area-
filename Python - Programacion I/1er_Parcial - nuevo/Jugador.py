from typing import Self
from Estadistica import Estadistica

class Jugador:

    # Constructor Jugador
    def __init__(self, jugador):
            self._nombre = jugador.get('nombre')
            self._posicion = jugador.get('posicion')
            self._stats = Estadistica(jugador.get('estadisticas'))
            self._logros = jugador.get('logros')

    def __str__(self):
        return f'{self.nombre}'
    
    def __repr__(self):
        return f'{self.logros}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def posicion(self):
        return self._posicion

    @posicion.setter
    def posicion(self, value):
        self._posicion = value

    @property
    def stats(self):
        return self._stats

    @stats.setter
    def stats(self, value):
        self._stats = value

    @property
    def logros(self):
        return self._logros

    @logros.setter
    def logros(self, value):
        self._logros = value

    def jugador_logros(self):
        """Imprime los logros de un jugador"""
        for logro in self.logros:
            print(logro)

    def calcular_valor(self):
        return (self.stats.robos_totales + self.stats.bloqueos_totales)

    def jugador_estaticas(self):
        """Imprime las estaticas de un jugador"""
        for stat in self.stats:
            print(f'{stat}, ')

    def convertir_diccionario(self):
        """Convierte el jugador en diccionario

        Returns:
            _type_: diccionario de jugador
        """
        return {'nombre' : self.nombre, 'posicion' : self.posicion, 'estadisticas' : self.stats.convertir_diccionario(), 'logros' : self.logros}