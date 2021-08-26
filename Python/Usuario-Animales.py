#<---- Clases y Herencias con Usuarios ---->#
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print("Hola, me llamo "  + self.nombre, self.apellido)


class Admin(Usuario):
    def saludoAdmin(self):
        print("Hola, me llamo " + self.nombre, self.apellido, "y soy admin.")
    


user = Usuario("Nano", "Jimenez")
admin = Admin("Lolo", "Fernandez")
#print(user.nombre, user.apellido)
#user.saludo()
#admin.saludo()
#admin.saludoAdmin()


#<---- Clases y Herencias con Animales ---->#
class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print("Hola, soy un", self.tipo, "y mi onomatopeya es", self.onomatopeya)

class Gato(Animal):
    tipo = "Gato"
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print("Se ha creado un gato.")

class Perro(Animal):
    tipo = "Perro"
    #Formas de extender algún elemento o función...
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print("Se ha creado un perro.")

class Canario(Animal):
    tipo = "Canario"

animal1 = Perro("Toby", "Guau")
animal2 = Gato("Orion", "Miau")
animal1.saludo()
animal2.saludo()

animal3 = Canario("Piolin", "Pío")
animal3.saludo()