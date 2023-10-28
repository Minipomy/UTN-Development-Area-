class Estadisticas:

    def __init__(self, stats:dict):
        self.seasons = stats['temporadas']
        self.total_points = stats['puntos_totales']
        self.average_points_per_match = stats['promedio_puntos_por_partido']
        self.total_bounces = stats['rebotes_totales']
        self.average_bounces_per_match = stats['promedio_rebotes_por_partido']
        self.total_assists = stats['asistencias_totales']
        self.average_assists_per_match = stats['promedio_asistencias_por_partido']
        self.total_theft = stats['robos_totales']
        self.total_blocks = stats['bloqueos_totales']
        self.percentaje_goal_throw = stats['porcentaje_tiros_de_campo']
        self.percentaje_free_throw = stats['porcentaje_tiros_libres']
        self.percentaje_triple_trow = stats['porcentaje_tiros_triples']

    def __repr__(self):
        return (f'Temporadas: {self.seasons},\nPuntos totales: {self.total_points},\nPromedio de puntos por partido: {self.average_points_per_match},\nRebotes totales: {self.total_bounces},\nPromedio de rebotes por partido: {self.average_bounces_per_match},\nAsistencias totales: {self.total_assists},\nPromedio de asistencias por partido: {self.average_assists_per_match},\nRobos totales: {self.total_theft},\nBloqueos totales: {self.total_blocks},\nPorcentaje de tiros de campo: {self.percentaje_goal_throw},\nPorcentaje de tiros libres: {self.percentaje_free_throw},\nPorcentaje de tiros triples: {self.percentaje_triple_trow}')

    # def show_stats(self):
    #     print(f'Temporadas: {self.seasons}')
    #     print(f'Puntos totales: {self.total_points}')
    #     print(f'Promedio de puntos por partido: {self.average_points_per_match}')
    #     print(f'Rebotes totales: {self.total_bounces}')
    #     print(f'Promedio de rebotes por partido: {self.average_bounces_per_match}')
    #     print(f'Asistencias totales: {self.total_assists}')
    #     print(f'Promedio de asistencias por partido: {self.average_assists_per_match}')
    #     print(f'Robos totales: {self.total_theft}')
    #     print(f'Bloqueos totales: {self.total_blocks}')
    #     print(f'Porcentaje de tiros de campo: {self.percentaje_goal_throw}')
    #     print(f'Porcentaje de tiros libres: {self.percentaje_free_throw}')
    #     print(f'Porcentaje de tiros triples: {self.percentaje_triple_trow}')

