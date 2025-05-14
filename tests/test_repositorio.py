import pytest
import os
from src.proceso import Proceso
from src.repositorio import RepositorioProcesos

def test_agregar_y_listar_procesos():
    repo = RepositorioProcesos()
    proceso = Proceso(pid="P1", duracion=10, prioridad=1)
    repo.agregar_proceso(proceso)
    assert len(repo.listar_procesos()) == 1

def test_eliminar_proceso():
    repo = RepositorioProcesos()
    proceso = Proceso(pid="P1", duracion=10, prioridad=1)
    repo.agregar_proceso(proceso)
    repo.eliminar_proceso("P1")
    assert len(repo.listar_procesos()) == 0

def test_obtener_proceso():
    repo = RepositorioProcesos()
    proceso = Proceso(pid="P1", duracion=10, prioridad=1)
    repo.agregar_proceso(proceso)
    assert repo.obtener_proceso("P1") == proceso

def test_guardar_y_cargar_json(tmp_path):
    repo = RepositorioProcesos()
    proceso = Proceso(pid="P1", duracion=10, prioridad=1)
    repo.agregar_proceso(proceso)
    archivo = tmp_path / "procesos.json"
    repo.guardar_en_json(archivo)
    repo.cargar_desde_json(archivo)
    assert len(repo.listar_procesos()) == 1

def test_guardar_y_cargar_csv(tmp_path):
    repo = RepositorioProcesos()
    proceso = Proceso(pid="P1", duracion=10, prioridad=1)
    repo.agregar_proceso(proceso)
    archivo = tmp_path / "procesos.csv"
    repo.guardar_en_csv(archivo)
    repo.cargar_desde_csv(archivo)
    assert len(repo.listar_procesos()) == 1
