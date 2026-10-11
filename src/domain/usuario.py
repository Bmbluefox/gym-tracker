class Usuario:
    def __init__(self, id_usuario: int, nombre: str, apellido: str, correo: str,):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.rutinas = []


    def agregar_rutina(self, rutina):
        self.rutinas.append(rutina)