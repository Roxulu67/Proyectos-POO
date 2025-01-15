class Personaje:  
    # Atributos de la clase
    # nombre = 'EstebanDido'
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0                                 
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
    # ¿Qué es self? Es una referencia al mismo objeto.
    # ¿Qué es el método init? Constructor que inicializa los atributos de un objeto.
    # ¿Por qué se usa doble guión bajo? Dunder. Porque es método mágico.
    # ¿Cuándo se ejecuta el método init? Automático. Al crear una nueva instancia u objeto.

    def imprimir_atributos(self):
        print(self.__nombre)
        print("-Fuerza:", self.__fuerza)
        print("-Inteligencia:", self.__inteligencia)
        print("-Defensa:", self.__defensa)
        print("-Vida:", self.__vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa
    
    def definir_vida(self):
        return self.__vida > 0
    
    def morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")

    def dañar(self, enemigo):
        # Se calcula el daño como la diferencia entre fuerza y defensa, asegurando que no sea menor que 0
        daño = self.__fuerza - enemigo.__defensa
        return max(daño, 0)  # Asegura que el daño no sea negativo
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        if daño > 0:  # Solo restamos vida si el daño es positivo
            enemigo.__vida -= daño
        print(self.__nombre, "ha atacado", daño, "puntos de daño a", enemigo.__nombre)
        print("Vida de", enemigo.__nombre, "es", enemigo.__vida)

    def get_vida(self):
        return self.__vida
    
    def set_vida(self, vida):
        self.__vida = vida
        #if self.__vida <=0:
            #self.morir()

# Variable del constructor vacío
mi_personaje = Personaje("EstebanDido", 40, 50, 45, 100)
mi_enemigo = Personaje("Ángel", 70, 100, 70, 100)
print(mi_personaje.get_vida())
# mi_personaje.set_vida(-5)
print(mi_personaje.get_vida())
mi_personaje._Personaje__vida = -50
mi_personaje.imprimir_atributos()
# mi_peronsaje.vida
# mi_personaje.__vida
# mi_personaje.vida=0
# mi_personaje.imprimir_atributos()
# mi_personaje.imprimir_atributos()
# mi_personaje.atacar(mi_enemigo)
# mi_personaje.morir()
# print(mi_personaje.definir_vida())
# mi_personaje.subir_nivel(15, 5, 10)
# print("Valores actualizados")
# mi_personaje.imprimir_atributos()

# Modificando valores de los atributos
# mi_personaje.__nombre = "EstebanDido"
# mi_personaje.__fuerza = 400
# mi_personaje.__inteligencia = 500
# mi_personaje.__defensa = 1000
# mi_personaje.__vida = 100

# print("El nombre de mi personaje es: ", mi_personaje.__nombre)
# print("El nombre de mi personaje es: ", mi_personaje.__fuerza)
# print("El nombre de mi personaje es: ", mi_personaje.__inteligencia)
# print("El nombre de mi personaje es: ", mi_personaje.__defensa)
# print("El nombre de mi personaje es: ", mi_personaje.__vida)