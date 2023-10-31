class Estadisticas:

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