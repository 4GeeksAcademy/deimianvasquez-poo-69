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



# # instacia de la clase
# deimian = Human("Deimian", "Vásquez", 25, "Male" )
# deimian.presentarse()
# print(deimian.serialize())
# deimian.arrancar()
# print(deimian.serialize())

class Trabajador(Human):
    def __init__(self, salario, profesion, human_nombre, human_apellido, human_edad, human_genero):
        super().__init__(human_nombre, human_apellido, human_edad, human_genero)
        self.__salario=salario
        self.profesion = profesion

    
    def __str__(self):
        return f"<class 'Trabajador' {self.nombre}>"

    def __repr__(self):
        return f"<__Trabajador__ {self.nombre}>"

    # def serialize(self):
    #     return{
    #         "Nombre": self.nombre,
    #         "Apellido": self.apellido,
    #         "Edad": self.edad,
    #         "Genero": self.genero,
    #         "Caminando": self.caminando,
    #         "Salario":self.salario,
    #         "Profesión": self.profesion
    #     }


    def serialize(self):
        return {
            **super().serialize(),
            "Salario": self.__salario,
            "Profesión": self.profesion
        }


    def cambiar_salario(self, nuevo_salario, user):
        # generar un registro de cambio de salario
        print(f"El uausrio que cambio el sueldo es: {'Deimian'}")
        self.__salario = nuevo_salario

    def consultar_salario(self):
        return self.__salario


deimian = Trabajador(1000, "Developer", "Deimian", "Vásquez", 25, "Male")
deimian.cambiar_salario(2000, {deimian})
print(deimian.serialize())



class Animal:
    def __init__(self, name, peso, especie, onomatopeya):
        self.peso = peso
        self.name = name
        self.especie = especie
        self.onomatopeya = onomatopeya


    def ruido(self):
        return f"Sonido: {self.onomatopeya}"

        
fifi = Animal("Fifi", "200gm", "Gato", "miauuu")
print(fifi.ruido())


firu = Animal("Muerdelo", "10kilos", "Perro", "guau")
print(firu.ruido())
