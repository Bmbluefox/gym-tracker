from src.domain.usuario import Usuario
from src.domain.rutina import Rutina
from src.domain.ejercicio import Ejercicio, TipoEjercicio, GrupoMuscular
from src.domain.serie import SerieFuerza, SerieCardio

def main():
    print("Iniciando simulador del Gym Tracker...\n")

    # 1. Creamos al usuario
    bauti = Usuario(
        id_usuario=1, 
        nombre="Bautista", 
        apellido="Sanchez", 
        correo="bauti@email.com"
    )

    # 2. Definimos los ejercicios (Usando tus Enums)
    sentadilla = Ejercicio(
        nombre="Sentadilla Búlgara", 
        tipo=TipoEjercicio.PESO_LIBRE, 
        grupo_muscular=GrupoMuscular.PIERNA
    )
    
    cinta = Ejercicio(
        nombre="Cinta de correr", 
        tipo=TipoEjercicio.CARDIO
        # No le pasamos grupo_muscular (será None por defecto, como lo programaste)
    )

    # 3. Creamos las series (Usando tus clases con herencia)
    serie_fuerza_1 = SerieFuerza(ejercicio=sentadilla, repeticiones=10, peso_kg=20.0)
    serie_fuerza_2 = SerieFuerza(ejercicio=sentadilla, repeticiones=8, peso_kg=24.0)
    
    # Serie de cardio: el constructor que armaste pide (ejercicio, distancia_km, tiempo_minutos)
    serie_cardio_1 = SerieCardio(ejercicio=cinta, distancia_km=3.5, tiempo_minutos=20.0)

    # 4. Creamos la rutina del día 
    # ATENCIÓN: Tu __init__ de Rutina pide una lista al final, por eso le paso []
    rutina_hoy = Rutina(
        nombre="Día de Piernas", 
        descripcion="Fuerza y un poco de resistencia al final", 
        ejercicios=[] 
    )

    # 5. Agregamos las series a la rutina
    rutina_hoy.agregar_ejercicio(serie_fuerza_1)
    rutina_hoy.agregar_ejercicio(serie_fuerza_2)
    rutina_hoy.agregar_ejercicio(serie_cardio_1)

    # 6. Guardamos la rutina en el usuario
    bauti.agregar_rutina(rutina_hoy)

    # 7. Imprimimos el resumen de entrenamiento
    print(f"--- Resumen de {bauti.nombre} {bauti.apellido} ---")
    
    # Podés usar el método "mostrar_rutina" que vos mismo escribiste en la clase Rutina,
    # pero como adentro de la rutina guardaste objetos Serie y no strings, el print 
    # se vería como objetos de memoria. 
    # Por eso, acá lo hacemos a mano usando el método "obtener_detalle()" que armaste en las series.
    
    print(f"Rutina: {rutina_hoy.nombre} | {rutina_hoy.descripcion}")
    print("Ejercicios completados:")
    
    # Recorremos la lista que guardaste en la rutina
    for serie in rutina_hoy.ejercicios:
        print(f" -> {serie.obtener_detalle()}")

if __name__ == "__main__":
    main()