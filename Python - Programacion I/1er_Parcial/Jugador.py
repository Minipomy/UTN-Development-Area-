from Estadisticas import Estadisticas

class Jugador:
    def __init__(self, player:list[dict]):
            self.name = player['nombre']
            self.position = player['posicion']
            self.stats = Estadisticas(player['estadisticas'])
            self.achievements = player['logros']
    
    def __repr__(self):
        return (f'Nombre: {self.name}, Posicion: {self.position}, Estadisticas: {self.stats}, Logros: {self.achievements}')
