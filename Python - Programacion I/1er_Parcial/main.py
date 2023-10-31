import json
import csv
import re as regex
from eng_strings import menu_initial_mensage, mm_bad_input, mm_save_stats, mm_search_by_name

class Estadistica:

    # Constructor Estadisticas
    def __init__(self, stats:dict):
        self.seasons = stats.get('temporadas')
        self.total_points = stats.get('puntos_totales')
        self.average_points_per_match = stats.get('promedio_puntos_por_partido')
        self.total_bounces = stats.get('rebotes_totales')
        self.average_bounces_per_match = stats.get('promedio_rebotes_por_partido')
        self.total_assists = stats.get('asistencias_totales')
        self.average_assists_per_match = stats.get('promedio_asistencias_por_partido')
        self.total_theft = stats.get('robos_totales')
        self.total_blocks = stats.get('bloqueos_totales')
        self.percentaje_goal_throw = stats.get('porcentaje_tiros_de_campo')
        self.percentaje_free_throw = stats.get('porcentaje_tiros_libres')
        self.percentaje_triple_trow = stats.get('porcentaje_tiros_triples')
        

    def __repr__(self):
        return (f'Temporadas: {self.seasons},\nPuntos totales: {self.total_points},\nPromedio de puntos por partido: {self.average_points_per_match},\nRebotes totales: {self.total_bounces},\nPromedio de rebotes por partido: {self.average_bounces_per_match},\nAsistencias totales: {self.total_assists},\nPromedio de asistencias por partido: {self.average_assists_per_match},\nRobos totales: {self.total_theft},\nBloqueos totales: {self.total_blocks},\nPorcentaje de tiros de campo: {self.percentaje_goal_throw},\nPorcentaje de tiros libres: {self.percentaje_free_throw},\nPorcentaje de tiros triples: {self.percentaje_triple_trow}')

class Jugador:

    # Constructor Jugador
    def __init__(self, player:list[dict]):
            self.name = player.get('nombre')
            self.position = player.get('posicion')
            self.stats = Estadistica(player.get('estadisticas'))
            self.achievements = player.get('logros')
    
    def __repr__(self):
        return (f'Nombre: {self.name}, Posicion: {self.position}\n\nEstadisticas: {self.stats}, Logros: {self.achievements}\n')
    
    def get_player_name_position(self) -> str:
        return (f'{self.name} - {self.position}')
    
    def print_achievements(self):
        print(f'Logros de {self.name}:')
        for triumphs in self.achievements:
            print(triumphs)

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

if __name__ == '__main__':
    team = Equipo('dream_team.json')

    flag = True
    while(flag):
        desired_option = 0
        digit_pattern = r'\b\d\b'
        name_pattern = r'<((?:[a-z]+|\s)*)>'
        menu_initial_mensage()
        try:
            desired_option = int(input())
        except ValueError as Error:
            print(f'Handled Error\n{Error}\n')

        match desired_option:
            case 1:
                team.print_players()
                input('Press enter key to continue...\n')
            case 2:
                optional = 'No'
                try:
                    chosen_player = int(input('Please, select a player by index\n'))
                    if regex.match(digit_pattern, str(chosen_player)):
                        print(team.players[chosen_player])
                        input('Press enter key to continue...\n')
                except ValueError as Error:
                    print(f'Handled Error\n{Error}\n')
                mm_save_stats()
                optional = input()
                if(optional.capitalize() == 'Yes'):
                    team.save_player_stats(chosen_player)
                    input('Saved...\nPress enter key to continue...\n')
            case 3:
                mm_search_by_name()
                try:
                    input_value = str(input())
                    team.search_player_by_name(input_value)
                except ValueError as Error:
                    print(f'Handled Error\n{Error}\n')
                input('Press enter key to continue...\n')
            case 4:pass
            case 5:pass
            case 6:
                flag = False