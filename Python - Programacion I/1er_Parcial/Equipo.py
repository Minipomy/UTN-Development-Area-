import json
from Jugador import Jugador

class Equipo:
    # Atributos Equipo
    
    # Constructor Equipo
    def __init__(self, json_file):
        with open(json_file, 'r', encoding="utf-8") as file:
            data = json.load(file)
        self.team_name = data['equipo']
        self.players = [Jugador(jugador) for jugador in data['jugadores']]

    def __repr__(self) -> str:
        return(f'Equipo: {self.team_name}, Jugadores: {self.players}')

    def get_players_position(self) -> str:
        for player in self.players:
            print(f'{player.name} - {player.position}')
    
    def select_player(self, index:int) -> str:
        if(index < 0 or index >= len(self.players)):
            print('Index-Out-Of-Range')
            return -1
        actual_player = self.players[index]
        print(f'{actual_player.name}\n\n{actual_player.stats}')
