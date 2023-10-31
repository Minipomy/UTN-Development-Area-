import re as regex
import json 
from Jugador import Jugador

class Equipo:
    # Constructor Equipo
    def __init__(self, json_file):
        with open(json_file, 'r', encoding="utf-8") as file:
            data = json.load(file)
        self.team_name = data.get('equipo')
        self.players = [Jugador(jugador) for jugador in data.get('jugadores')]

    def __repr__(self) -> str:
        return(f'Equipo: {self.team_name}, Jugadores: {self.players}')

    def print_players(self) -> str:
        for index, player in enumerate(self.players):
            print(f'{index}.- {player.get_player_name_position()}')

    def select_player(self, index:int) -> str:
        player = self.players[index]
        print(f'''{player.name}\n\n{player.stats}''')

    def save_player_stats(self, index:int):
        player = self.players[index]
        with open(f'{player.name} - Stats.csv', mode="w", newline="") as csv_file:
            column_names = ['nombre', 'posicion', 'temporadas', 'puntos_totales', 'promedio_puntos_por_partido',
                          'rebotes_totales', 'promedio_rebotes_por_partido', 'asistencias_totales',
                          'promedio_asistencias_por_partido', 'robos_totales', 'bloqueos_totales',
                          'porcentaje_tiros_de_campo', 'porcentaje_tiros_libres', 'porcentaje_tiros_triples']
            write = csv.DictWriter(csv_file, fieldnames=column_names)
            write.writeheader()
            write.writerow({'nombre': player.name,
                             'posicion': player.position,
                             'temporadas': player.stats.seasons,
                             'puntos_totales': player.stats.total_points,
                             'promedio_puntos_por_partido': player.stats.average_points_per_match,
                             'rebotes_totales': player.stats.total_bounces,
                             'promedio_rebotes_por_partido': player.stats.average_bounces_per_match,
                             'asistencias_totales': player.stats.total_assists,
                             'promedio_asistencias_por_partido': player.stats.average_assists_per_match,
                             'robos_totales': player.stats.total_theft,
                             'bloqueos_totales': player.stats.total_blocks,
                             'porcentaje_tiros_de_campo': player.stats.percentaje_goal_throw,
                             'porcentaje_tiros_libres': player.stats.percentaje_free_throw,
                             'porcentaje_tiros_triples': player.stats.percentaje_triple_trow})

    def search_player_by_name(self, name:str):
        re = regex.compile(name, regex.IGNORECASE)
        for index, jugador in enumerate(self.players):
            if re.findall(jugador.name):
                self.select_player(index)
                # print('Error -Player not found-')