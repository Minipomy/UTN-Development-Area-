from Estadisticas import Estadisticas

class Jugador:

    # Constructor Jugador
    def __init__(self, player:list[dict]):
            self.name = player.get('nombre')
            self.position = player.get('posicion')
            self.stats = Estadisticas(player.get('estadisticas'))
            self.achievements = player.get('logros')
    
    def __repr__(self):
        return (f'Nombre: {self.name}, Posicion: {self.position}\n\nEstadisticas: {self.stats}, Logros: {self.achievements}\n')
    
    def get_player_name_position(self) -> str:
        return (f'{self.name} - {self.position}')
    
    def print_achievements(self):
        print(f'Logros de {self.name}:')
        for triumphs in self.achievements:
            print(triumphs)