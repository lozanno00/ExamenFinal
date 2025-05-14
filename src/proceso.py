from typing import Optional

class Proceso:
    procesos_existentes = set()  # Para validar unicidad de PID

    def __init__(self, pid: str, duracion: int, prioridad: int):
        if not pid or pid in Proceso.procesos_existentes:
            raise ValueError("El PID debe ser único y no vacío.")
        if duracion <= 0:
            raise ValueError("La duración debe ser un entero positivo.")
        if prioridad < 0:
            raise ValueError("La prioridad debe ser un entero no negativo.")

        self.pid = pid
        self.duracion = duracion
        self.prioridad = prioridad
        self.tiempo_restante = duracion
        self.tiempo_llegada = 0  # Asumido como 0
        self.tiempo_inicio: Optional[int] = None
        self.tiempo_fin: Optional[int] = None

        Proceso.procesos_existentes.add(pid)

    def __repr__(self):
        return (f"Proceso(pid={self.pid}, duracion={self.duracion}, "
                f"prioridad={self.prioridad})")
