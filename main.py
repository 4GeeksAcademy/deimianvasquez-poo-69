class Human:
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.caminando=False


    def __str__(self):
        return f"<class 'Human'{self.nombre}>"


    def __repr__(self):
        return f"<__Human__ {self.nombre}>"


    def presentarse(self):
        print(f"Hola ¿qué tal ? Mi nombre es {self.nombre} {self.apellido}")


    def arrancar(self):
        self.caminando = True


    def detener(self):
        self.caminando = False


    def serialize(self):
        return{
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "Edad": self.edad,
            "Genero": self.genero,
            "Caminando": self.caminando
        }




juan = Human("Juancito","Vásquez", 20, "Masculino")
print(juan.serialize())
juan.arrancar()
print(juan.serialize())
juan.detener()
print(juan.serialize())



deimian = Human("Deimian","Vásquez", 25, "Masculino")
# print(deimian.presentarse())