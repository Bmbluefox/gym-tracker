from enum import Enum
from typing import Optional

class TipoEjercicio(Enum):
    CARDIO = "Cardio"
    PESO_LIBRE = "Peso Libre"
    PESO_CORPORAL = "Peso Corporal"
    MAQUINA = "Máquina"
    POLEA = "Polea"


class GrupoMuscular(Enum):
    PECHO = "Pecho"
    ESPALDA = "Espalda"
    PIERNA = "Pierna"
    HOMBRO = "Hombro"
    BRAZO = "Brazo"
    CORE = "Core"

class Ejercicio:
    def __init__(self, nombre: str, tipo: TipoEjercicio, grupo_muscular: Optional[GrupoMuscular] = None):
       
        if tipo == TipoEjercicio.CARDIO and grupo_muscular is not None:
            raise ValueError("Los ejercicios de tipo 'Cardio' no deben tener un grupo muscular asociado.")
        if tipo != TipoEjercicio.CARDIO and grupo_muscular is None:
            raise ValueError("Los ejercicios que no son de tipo 'Cardio' deben tener un grupo muscular asociado.")
       
        self.nombre = nombre
        self.tipo = tipo
        self.grupo_muscular = grupo_muscular

    def __str__(self):
        return f"{self.nombre} ({self.tipo.value}, {self.grupo_muscular.value})"