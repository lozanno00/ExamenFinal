def calcular_tiempo_respuesta(procesos):
    """Calcula el tiempo de respuesta promedio."""
    return sum(p.tiempo_inicio - p.tiempo_llegada for p in procesos) / len(procesos)

def calcular_tiempo_retorno(procesos):
    """Calcula el tiempo de retorno promedio."""
    return sum(p.tiempo_fin - p.tiempo_llegada for p in procesos) / len(procesos)

def calcular_tiempo_espera(procesos):
    """Calcula el tiempo de espera promedio."""
    return sum((p.tiempo_fin - p.tiempo_llegada) - p.duracion for p in procesos) / len(procesos)
