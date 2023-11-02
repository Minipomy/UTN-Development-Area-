class Estadistica:

    # Constructor Estadistica
    def __init__(self, stats) -> None:            
        self._temporadas = stats.get('temporadas')
        self._puntos_totales = stats.get('puntos_totales')
        self._promedio_puntos_por_partido = stats.get('promedio_puntos_por_partido')
        self._rebotes_totales = stats.get('rebotes_totales')
        self._promedio_rebotes_por_partido = stats.get('promedio_rebotes_por_partido')
        self._asistencias_totales = stats.get('asistencias_totales')
        self._promedio_asistencias_por_partido = stats.get('promedio_asistencias_por_partido')
        self._robos_totales = stats.get('robos_totales')
        self._bloqueos_totales = stats.get('bloqueos_totales')
        self._porcentaje_tiros_de_campo = stats.get('porcentaje_tiros_de_campo')
        self._porcentaje_tiros_libres = stats.get('porcentaje_tiros_libres')
        self._porcentaje_tiros_triples = stats.get('porcentaje_tiros_triples')

    def __str__(self):
        return (f'Temporadas: {self.temporadas},\nPuntos totales: {self.puntos_totales},\nPromedio de puntos por partido: {self.promedio_puntos_por_partido},\nRebotes totales: {self.rebotes_totales},\nPromedio de rebotes por partido: {self.promedio_rebotes_por_partido},\nAsistencias totales: {self.asistencias_totales},\nPromedio de asistencias por partido: {self.promedio_asistencias_por_partido},\nRobos totales: {self.robos_totales},\nBloqueos totales: {self.bloqueos_totales},\nPorcentaje de tiros de campo: {self.porcentaje_tiros_de_campo},\nPorcentaje de tiros libres: {self.porcentaje_tiros_libres},\nPorcentaje de tiros triples: {self.porcentaje_tiros_triples}')

    # Getters
    @property
    def temporadas(self):
        return self._temporadas

    @property
    def puntos_totales(self):
        return self._puntos_totales

    @property
    def promedio_puntos_por_partido(self):
        return self._promedio_puntos_por_partido

    @property
    def rebotes_totales(self):
        return self._rebotes_totales

    @property
    def promedio_rebotes_por_partido(self):
        return self._promedio_rebotes_por_partido

    @property
    def asistencias_totales(self):
        return self._asistencias_totales

    @property
    def promedio_asistencias_por_partido(self):
        return self._promedio_asistencias_por_partido

    @property
    def robos_totales(self):
        return self._robos_totales

    @property
    def bloqueos_totales(self):
        return self._bloqueos_totales

    @property
    def porcentaje_tiros_de_campo(self):
        return self._porcentaje_tiros_de_campo

    @property
    def porcentaje_tiros_libres(self):
        return self._porcentaje_tiros_libres

    @property
    def porcentaje_tiros_triples(self):
        return self._porcentaje_tiros_triples

    # Setters
    @temporadas.setter
    def temporadas(self, value):
        self._temporadas = value

    @puntos_totales.setter
    def puntos_totales(self, value):
        self._puntos_totales = value

    @promedio_puntos_por_partido.setter
    def promedio_puntos_por_partido(self, value):
        self._promedio_puntos_por_partido = value

    @rebotes_totales.setter
    def rebotes_totales(self, value):
        self._rebotes_totales = value

    @promedio_rebotes_por_partido.setter
    def promedio_rebotes_por_partido(self, value):
        self._promedio_rebotes_por_partido = value

    @asistencias_totales.setter
    def asistencias_totales(self, value):
        self._asistencias_totales = value

    @promedio_asistencias_por_partido.setter
    def promedio_asistencias_por_partido(self, value):
        self._promedio_asistencias_por_partido = value

    @robos_totales.setter
    def robos_totales(self, value):
        self._robos_totales = value

    @bloqueos_totales.setter
    def bloqueos_totales(self, value):
        self._bloqueos_totales = value

    @porcentaje_tiros_de_campo.setter
    def porcentaje_tiros_de_campo(self, value):
        self._porcentaje_tiros_de_campo = value

    @porcentaje_tiros_libres.setter
    def porcentaje_tiros_libres(self, value):
        self._porcentaje_tiros_libres = value

    @porcentaje_tiros_triples.setter
    def porcentaje_tiros_triples(self, value):
        self._porcentaje_tiros_triples = value

    def convertir_diccionario(self):
        """Convierte las estadisticas en diccionario

        Returns:
            _type_: devuelve las estadisticas en forma de diccionario
        """
        return {'temporadas': self.temporadas,\
                'puntos_totales': self.puntos_totales,\
                'promedio_puntos_por_partido':self.promedio_puntos_por_partido,\
                'rebotes_totales':self.rebotes_totales,\
                'promedio_rebotes_por_partido':self.promedio_rebotes_por_partido,\
                'asistencias_totales':self.asistencias_totales,\
                'promedio_asistencias_por_partido':self.promedio_asistencias_por_partido,\
                'robos_totales':self.robos_totales,\
                'bloqueos_totales':self.bloqueos_totales,\
                'porcentaje_tiros_de_campo':self.porcentaje_tiros_de_campo,\
                'porcentaje_tiros_libres':self.porcentaje_tiros_libres,\
                'porcentaje_tiros_triples':self.porcentaje_tiros_triples}