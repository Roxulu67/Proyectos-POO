class Personaje:  
    # Atributos de la clase
    # nombre = 'EstebanDido'
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0                                 
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    # ¿Qué es self? Es una referencia al mismo objeto.
    # ¿Qué es el método init? Constructor que inicializa los atributos de un objeto.
    # ¿Por qué se usa doble guión bajo? Dunder. Porque es método mágico.
    # ¿Cuándo se ejecuta el método init? Automático. Al crear una nueva instancia u objeto.

    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Defensa:", self.defensa)
        print("-Vida:", self.vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    
    def definir_vida(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def dañar(self, enemigo):
        # Se calcula el daño como la diferencia entre fuerza y defensa, asegurando que no sea menor que 0
        daño = self.fuerza - enemigo.defensa
        return max(daño, 0)  # Asegura que el daño no sea negativo
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        if daño > 0:  # Solo restamos vida si el daño es positivo
            enemigo.vida -= daño
        print(self.nombre, "ha atacado", daño, "puntos de daño a", enemigo.nombre)
        print("Vida de", enemigo.nombre, "es", enemigo.vida)

class Guerrero(Personaje):
    pass

    #Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida,espada):
        super().__init__(nombre,fuerza,inteligencia,defensa, vida)
        self.espada = espada

arturoSuarez = Guerrero("Arturo Suarez",12,3000,2,100,.5)
arturoSuarez.imprimir_atributos()
print("El valor de espada: ", arturoSuarez.espada)

# Variable del constructor vacío
mi_personaje = Personaje("EstebanDido", 40, 50, 45, 100)
mi_enemigo = Personaje("Ángel", 70, 100, 70, 100)
#mi_personaje.imprimir_atributos()
#mi_personaje.atacar(mi_enemigo)
# mi_personaje.morir()
# print(mi_personaje.definir_vida())
# mi_personaje.subir_nivel(15, 5, 10)
# print("Valores actualizados")
# mi_personaje.imprimir_atributos()

# Modificando valores de los atributos
# mi_personaje.nombre = "EstebanDido"
# mi_personaje.fuerza = 400
# mi_personaje.inteligencia = 500
# mi_personaje.defensa = 1000
# mi_personaje.vida = 100

# print("El nombre de mi personaje es: ", mi_personaje.nombre)
# print("El nombre de mi personaje es: ", mi_personaje.fuerza)
# print("El nombre de mi personaje es: ", mi_personaje.inteligencia)
# print("El nombre de mi personaje es: ", mi_personaje.defensa)
# print("El nombre de mi personaje es: ", mi_personaje.vida)