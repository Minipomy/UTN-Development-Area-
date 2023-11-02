def ui_menu() -> str:
    mensaje = """
1.- Listar todos los jugadores del equipo Dream Team.
2.- Seleccionar un jugador por su indice y mostrar estadisticas. Permite guardar los datos en un CSV (Opcional)
3.- Buscar jugador por nombre y mostrar sus estadisticas.
4.- Calcular y mostrar el promedio de puntos por partido de todo el equipo Dream Team
5.- Buscar jugador por nombre y validar si pertenece al salon de la fama del Baloncesto.
6.- Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
7.- Segun numero de DNI
8.- Ordenar y listar los jugadores por la suma de robos totales y bloqueos totales
9.- Salir\n"""
    print (mensaje)

def ui_option() -> str:
    mensaje = """
Por favor, ingresar un valor que figura en pantalla\n"""
    return mensaje

def ui_continue() -> str:
    mensaje = """
Por favor, apretar ENTER para continuar\n"""
    return mensaje

def ui_error(error:str) -> str:
    return f"""Exception Handled\n{error}"""

def ui_save_csv() -> str:
    mensaje = """
Desea guardar los datos selecionados en un CSV? Yes/No\n"""
    return mensaje

def ui_save_json() -> str:
    mensaje = """
Desea guardar los datos selecionados en un JSON? Yes/No\n"""
    return mensaje

def ui_data_saved() -> str:
    mensaje = """
Datos guardados...\n"""
    return mensaje

def ui_escribir_nombre() -> str:
    mensaje = """
Por favor, escribir el nombre\n"""
    return mensaje

def ui_como_ordenar_valores() -> str:
    mensaje = """
Por favor, especificar como desea ordenar los valores? Desc/Asc\n"""
    return mensaje