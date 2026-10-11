from abc import ABC, abstractmethod
from src.domain.ejercicio import Ejercicio, TipoEjercicio 

class Serie(ABC):
    def __init__(self, ejercicio: Ejercicio):
        self.ejercicio = ejercicio


    @abstractmethod
    def obtener_detalle(self) -> str:
        pass

class SerieFuerza(Serie):
    def __init__(self, ejercicio: Ejercicio, repeticiones: int, peso_kg: float = 0.0):

        if ejercicio.tipo == TipoEjercicio.CARDIO:
            raise ValueError("No se puede crear una SerieFuerza para un ejercicio de tipo 'Cardio'.")

        super().__init__(ejercicio)
        self.repeticiones = repeticiones
        self.peso_kg = peso_kg

    def obtener_detalle(self) -> str:
        return f"Serie de fuerza: {self.ejercicio.nombre}, Repeticiones: {self.repeticiones}, Peso: {self.peso_kg} kg"


class SerieCardio(Serie):
    def __init__(self, ejercicio: Ejercicio, distancia_km: float, tiempo_minutos: float):
        if ejercicio.tipo != TipoEjercicio.CARDIO:
            raise ValueError("No se puede crear una SerieCardio para un ejercicio que no sea de tipo 'Cardio'.")

        super().__init__(ejercicio)
        self.distancia_km = distancia_km
        self.tiempo_minutos = tiempo_minutos

    def obtener_detalle(self) -> str:
        return f"Serie de cardio: {self.ejercicio.nombre}, Distancia: {self.distancia_km} km, Tiempo: {self.tiempo_minutos} minutos"