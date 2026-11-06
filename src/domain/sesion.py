from datetime import datetime
from src.domain.ejercicio import Ejercicio
from src.domain.serie import Serie
from src.domain.rutina import Rutina

class EjercicioRealizado:
    def __init__(self, ejercicio: Ejercicio):
        self.ejercicio = ejercicio
        self.series_completadas = []

    def registrar_serie(self, serie: Serie):
        self.series_completadas.append(serie)


class Sesion:
    def __init__(self, rutina_base: Rutina):
        self.rutina_base = rutina_base
        self.fecha = datetime.now()
        self.duracion_minutos = 0

        self.ejercicios_realizados = []
        for ej_planeado in rutina_base.ejercicios:
            nuevo_registro = EjercicioRealizado(ejercicio=ej_planeado)
            self.ejercicios_realizados.append(nuevo_registro)

    def agregar_ejercicio_extra(self, nuevo_ejercicio: Ejercicio):
        nuevo_registro = EjercicioRealizado(ejercicio=nuevo_ejercicio)
        self.ejercicios_realizados.append(nuevo_registro)

    def quitar_ejercicio(self, nombre_ejercicio: str):
        for registro in self.ejercicios_realizados:
            if registro.ejercicio.nombre == nombre_ejercicio:
                self.ejercicios_realizados.remove(registro)
                break

    def reemplazar_ejercicio(self, nombre_viejo: str, ejercicio_nuevo: Ejercicio):
        self.quitar_ejercicio(nombre_ejercicio=nombre_viejo)
        self.agregar_ejercicio_extra(nuevo_ejercicio=ejercicio_nuevo)

    def terminar_sesion(self, duracion: int):
        self.duracion_minutos = duracion

