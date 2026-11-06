from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Importamos todas las piezas de tu dominio
from src.domain.ejercicio import Ejercicio, TipoEjercicio, GrupoMuscular
from src.domain.rutina import Rutina
from src.domain.sesion import Sesion
from src.domain.serie import SerieFuerza

app = FastAPI(title="App de Gimnasio - Ejecución en Vivo")

# --- 1. DATOS DE PRUEBA (Simulando lo que vendría de una base de datos) ---
ejercicio_pecho = Ejercicio("Press de Banca", TipoEjercicio.PESO_LIBRE, GrupoMuscular.PECHO)
ejercicio_pierna = Ejercicio("Sentadilla", TipoEjercicio.PESO_LIBRE, GrupoMuscular.PIERNA)
rutina_prueba = Rutina("Día de Fuerza", "Torso/Pierna básico", [ejercicio_pecho, ejercicio_pierna], descanso_por_defecto=90)

# Esta variable simulará la memoria de tu teléfono mientras entrenas
sesion_actual = None

# --- 2. TRADUCTOR ---
# Lo que enviaremos desde los botones de la app cuando terminemos una serie
class DatosSerieNueva(BaseModel):
    repeticiones: int
    peso_kg: float
    descanso_segundos: int = 90 # Si no lo tocas, asume 90. Si lo cambias, usa el nuevo.

# --- 3. RUTAS DE LA API ---

@app.post("/sesion/iniciar")
def iniciar_sesion():
    global sesion_actual
    # Hacemos la fotocopia de la rutina para empezar a rayarla
    sesion_actual = Sesion(rutina_base=rutina_prueba)
    ejercicios = [reg.ejercicio.nombre for reg in sesion_actual.ejercicios_realizados]
    return {"mensaje": "¡Entrenamiento iniciado!", "ejercicios_de_hoy": ejercicios}

@app.get("/sesion")
def ver_sesion_actual():
    if not sesion_actual:
        return {"mensaje": "No estás entrenando en este momento."}
    
    # Armamos un resumen visual de todo lo que transpiraste hasta ahora
    resumen = []
    for registro in sesion_actual.ejercicios_realizados:
        series_texto = [serie.obtener_detalle() for serie in registro.series_completadas]
        resumen.append({
            "ejercicio": registro.ejercicio.nombre,
            "series": series_texto
        })
    return {"estado": resumen}

@app.delete("/sesion/ejercicios/{nombre_ejercicio}")
def quitar_ejercicio(nombre_ejercicio: str):
    if not sesion_actual:
        raise HTTPException(status_code=400, detail="Inicia sesión primero.")
        
    sesion_actual.quitar_ejercicio(nombre_ejercicio)
    return {"mensaje": f"Tachaste '{nombre_ejercicio}' de la lista de hoy."}

@app.post("/sesion/ejercicios/{nombre_ejercicio}/series")
def registrar_serie_completada(nombre_ejercicio: str, datos: DatosSerieNueva):
    if not sesion_actual:
        raise HTTPException(status_code=400, detail="Inicia sesión primero.")
        
    # Buscamos en qué ejercicio específico acabas de anotar la serie
    for registro in sesion_actual.ejercicios_realizados:
        if registro.ejercicio.nombre == nombre_ejercicio:
            
            # Creamos TU serie, con su propio peso y su propio timer independiente
            nueva_serie = SerieFuerza(
                ejercicio=registro.ejercicio,
                repeticiones=datos.repeticiones,
                peso_kg=datos.peso_kg,
                descanso_segundos=datos.descanso_segundos
            )
            nueva_serie.marcar_completada()
            registro.registrar_serie(nueva_serie)
            
            return {"mensaje": "¡Serie anotada!", "detalle": nueva_serie.obtener_detalle()}
            
    raise HTTPException(status_code=404, detail="Ese ejercicio no está en tu rutina de hoy.")
