from src.proceso import Proceso
from src.metrics import calcular_tiempo_respuesta, calcular_tiempo_retorno, calcular_tiempo_espera

def test_calculo_metricas():
    procesos = [
        Proceso(pid="P1", duracion=5, prioridad=1),
        Proceso(pid="P2", duracion=3, prioridad=2),
    ]
    procesos[0].tiempo_inicio = 0
    procesos[0].tiempo_fin = 5
    procesos[1].tiempo_inicio = 5
    procesos[1].tiempo_fin = 8

    assert calcular_tiempo_respuesta(procesos) == 2.5
    assert calcular_tiempo_retorno(procesos) == 5.5
    assert calcular_tiempo_espera(procesos) == 2.5
