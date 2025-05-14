import sys
from src.proceso import Proceso
from src.repositorio import RepositorioProcesos
from src.scheduler import FCFSScheduler, RoundRobinScheduler

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar proceso")
    print("2. Listar procesos")
    print("3. Seleccionar algoritmo de planificación")
    print("4. Ejecutar simulación")
    print("5. Guardar procesos")
    print("6. Cargar procesos")
    print("7. Salir")

def main():
    repo = RepositorioProcesos()
    scheduler = None

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pid = input("Ingrese el PID: ")
            duracion = int(input("Ingrese la duración: "))
            prioridad = int(input("Ingrese la prioridad: "))
            try:
                proceso = Proceso(pid=pid, duracion=duracion, prioridad=prioridad)
                repo.agregar_proceso(proceso)
                print("Proceso agregado exitosamente.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            procesos = repo.listar_procesos()
            if not procesos:
                print("No hay procesos registrados.")
            else:
                print("\nProcesos registrados:")
                for p in procesos:
                    print(f"PID: {p.pid}, Duración: {p.duracion}, Prioridad: {p.prioridad}")

        elif opcion == "3":
            print("\nSeleccione un algoritmo de planificación:")
            print("1. FCFS (First-Come, First-Served)")
            print("2. Round-Robin")
            algoritmo = input("Seleccione una opción: ")
            if algoritmo == "1":
                scheduler = FCFSScheduler()
                print("Algoritmo FCFS seleccionado.")
            elif algoritmo == "2":
                quantum = int(input("Ingrese el quantum para Round-Robin: "))
                scheduler = RoundRobinScheduler(quantum=quantum)
                print("Algoritmo Round-Robin seleccionado.")
            else:
                print("Opción inválida.")

        elif opcion == "4":
            if not scheduler:
                print("Debe seleccionar un algoritmo de planificación primero.")
            else:
                procesos = repo.listar_procesos()
                if not procesos:
                    print("No hay procesos para planificar.")
                else:
                    gantt = scheduler.planificar(procesos)
                    print("\nDiagrama de Gantt:")
                    for entry in gantt:
                        print(f"PID: {entry[0]}, Inicio: {entry[1]}, Fin: {entry[2]}")

        elif opcion == "5":
            formato = input("Seleccione el formato (json/csv): ").lower()
            archivo = input("Ingrese el nombre del archivo: ")
            if formato == "json":
                repo.guardar_en_json(archivo)
                print("Procesos guardados en JSON.")
            elif formato == "csv":
                repo.guardar_en_csv(archivo)
                print("Procesos guardados en CSV.")
            else:
                print("Formato inválido.")

        elif opcion == "6":
            formato = input("Seleccione el formato (json/csv): ").lower()
            archivo = input("Ingrese el nombre del archivo: ")
            if formato == "json":
                repo.cargar_desde_json(archivo)
                print("Procesos cargados desde JSON.")
            elif formato == "csv":
                repo.cargar_desde_csv(archivo)
                print("Procesos cargados desde CSV.")
            else:
                print("Formato inválido.")

        elif opcion == "7":
            print("Saliendo del programa...")
            sys.exit()

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
