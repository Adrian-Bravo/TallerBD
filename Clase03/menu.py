class Persona():
    def __init__(self):
        self.personas = {}

    def agregarPersonas(self):
        self.codigo = input("Codigo: ")
        if self.codigo in self.personas:
            print("Este codigo ya existe.")
        else:
            self.nombre = input("Nombre: ")
            self.edad = input("Edad: ")
            self.personas[self.codigo] = (self.nombre, self.edad)

    def eliminarPersonas(self):
        if len(self.personas) == 0:
            print("No hay nada para eliminar.")
        else:
            self.cod = input("Ingrese el codigo de la persona que desea eliminar => ")
            if (self.cod in self.personas):
                print(f"Se eliminó {self.personas.pop(self.cod)}")
            else:
                print("Este codigo no existe")

    def mostrarPersonas(self):
        if len(self.personas) == 0:
            print("La lista está vacia")
        else:
            for i, v in self.personas.items():
                print(f"{i}: {v}")