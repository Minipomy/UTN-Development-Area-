from Equipo import Equipo
from strings import ui_continue, ui_data_saved, ui_escribir_nombre, ui_menu, ui_option, ui_error, ui_save_csv, ui_como_ordenar_valores, ui_save_json


if __name__ == "__main__":
    dream = Equipo('dream_team.json')
    flag = True

    while(flag):
        ui_menu()
        try:
            opcion_ingresada = int(input(ui_option()))
            match opcion_ingresada:
                    case 1:
                        dream.listar_jugadores_posicion()
                        input(ui_continue())
                    case 2:
                        try:
                            optional = 'No'
                            dream.listar_jugadores_posicion()
                            valor = int(input(ui_option()))
                            dream.seleccionar_jugador(valor)
                            optional = str(input(ui_save_csv()))
                            if(optional.lower().capitalize() == 'Yes' or optional.lower().capitalize() == 'Y'):
                                dream.save_csv(valor)
                        except ValueError as error:
                            ui_error(error)
                    case 3:
                        nombre = input(ui_escribir_nombre())
                        dream.buscar_jugador_por_nombre(nombre)
                        input(ui_continue())
                    case 4:
                        dream.mostrar_promedios()
                        input(ui_continue())
                    case 5:
                        nombre = input(ui_escribir_nombre())
                        dream.salon_de_la_fama(nombre)
                        input(ui_continue())
                    case 6:
                        dream.mayor_rebotes()
                        input(ui_continue())
                    case 7:
                        try:
                            valor = str(input(ui_como_ordenar_valores())).capitalize()
                            dream.ordenar_jugadores(valor)
                            try:
                                optional = str(input(ui_save_json())).lower().capitalize()
                                if(optional == 'Yes' or optional == 'Y'):
                                    valor = str(input(ui_escribir_nombre()))
                                    dream.save_json_MAXIMILIANO(valor)
                                    input(ui_data_saved())
                            except ValueError as error:
                                ui_error(error)
                        except ValueError as error:
                            ui_error(error)
                    case 8:
                        dream.orden_sumando_valores()
                        input(ui_continue())
                    case 9:
                        flag = False
        except ValueError as error:
            ui_error(error)