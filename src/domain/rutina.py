class Rutina:
    def __init__(self, nombre: str, descripcion: str, ejercicios: list):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ejercicios = ejercicios

    def agregar_ejercicio(self, ejercicio):
        self.ejercicios.append(ejercicio)

    def eliminar_ejercicio(self, ejercicio):
        if ejercicio in self.ejercicios:
            self.ejercicios.remove(ejercicio)

    def mostrar_rutina(self):
        print(f"Rutina: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print("Ejercicios:")
        for ejercicio in self.ejercicios:
            print(f"- {ejercicio}")