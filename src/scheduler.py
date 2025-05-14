from abc import ABC, abstractmethod
from typing import List, Tuple
from src.proceso import Proceso

GanttEntry = Tuple[str, int, int]  # (PID, tiempo_inicio, tiempo_fin)

class Scheduler(ABC):
    @abstractmethod
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        """Planifica los procesos y devuelve un diagrama de Gantt."""
        pass

class FCFSScheduler(Scheduler):
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        gantt = []
        tiempo_actual = 0

        for proceso in sorted(procesos, key=lambda p: p.tiempo_llegada):
            proceso.tiempo_inicio = tiempo_actual
            proceso.tiempo_fin = tiempo_actual + proceso.duracion
            gantt.append((proceso.pid, proceso.tiempo_inicio, proceso.tiempo_fin))
            tiempo_actual = proceso.tiempo_fin

        return gantt

class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum: int):
        if quantum <= 0:
            raise ValueError("El quantum debe ser un entero positivo.")
        self.quantum = quantum

    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        gantt = []
        cola = procesos[:]
        tiempo_actual = 0

        while cola:
            proceso = cola.pop(0)
            if proceso.tiempo_restante > self.quantum:
                gantt.append((proceso.pid, tiempo_actual, tiempo_actual + self.quantum))
                tiempo_actual += self.quantum
                proceso.tiempo_restante -= self.quantum
                cola.append(proceso)
            else:
                gantt.append((proceso.pid, tiempo_actual, tiempo_actual + proceso.tiempo_restante))
                tiempo_actual += proceso.tiempo_restante
                proceso.tiempo_restante = 0
                proceso.tiempo_fin = tiempo_actual

        return gantt
