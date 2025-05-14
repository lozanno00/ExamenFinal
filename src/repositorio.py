import json
import csv
from src.proceso import Proceso

class RepositorioProcesos:
    def __init__(self):
        self.procesos = {}

    def agregar_proceso(self, proceso: Proceso):
        if proceso.pid in self.procesos:
            raise ValueError(f"El proceso con PID {proceso.pid} ya existe.")
        self.procesos[proceso.pid] = proceso

    def listar_procesos(self):
        return list(self.procesos.values())

    def eliminar_proceso(self, pid: str):
        if pid not in self.procesos:
            raise ValueError(f"No se encontró un proceso con PID {pid}.")
        del self.procesos[pid]

    def obtener_proceso(self, pid: str):
        return self.procesos.get(pid, None)

    def guardar_en_json(self, archivo: str):
        with open(archivo, 'w') as f:
            json.dump([proceso.__dict__ for proceso in self.procesos.values()], f)

    def cargar_desde_json(self, archivo: str):
        with open(archivo, 'r') as f:
            datos = json.load(f)
            self.procesos = {p['pid']: Proceso(**p) for p in datos}

    def guardar_en_csv(self, archivo: str):
        with open(archivo, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['pid', 'duracion', 'prioridad'])
            for proceso in self.procesos.values():
                writer.writerow([proceso.pid, proceso.duracion, proceso.prioridad])

    def cargar_desde_csv(self, archivo: str):
        with open(archivo, 'r') as f:
            reader = csv.DictReader(f, delimiter=';')
            self.procesos = {
                row['pid']: Proceso(
                    pid=row['pid'],
                    duracion=int(row['duracion']),
                    prioridad=int(row['prioridad'])
                )
                for row in reader
            }
