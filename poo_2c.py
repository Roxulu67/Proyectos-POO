class personaje:
    # Atributos de la clase
    # nombre = "Default"
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0

    # Constructor de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    # ¿Qué es self? Es una referencia al mismo objeto
    # ¿Qué es el método __init__? Es un constructor que inicializa los atributos de un objeto
    # ¿Por qué se usa doble guion bajo? Porque es un método mágico
    # ¿Cuándo se ejecuta el método __init__? Automáticamente al crear una nueva instancia u objeto
    # ¿Qué es polimorfismo? Es un mismo método que puede tener diferente comportamiento dependiendo del objeto que lo llame

    # Método para imprimir los atributos
    def imprimir_atributos(self):
        print(self.nombre)
        print("- fuerza:", self.fuerza)
        print("- inteligencia:", self.inteligencia)
        print("- defensa:", self.defensa)
        print("- vida:", self.vida)

    # Método para subir nivel
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    # Método para verificar si está vivo
    def está_vivo(self):
        return self.vida > 0

    # Método para "morir"
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    # Método para calcular daño
    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa

    # Método para atacar
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        if daño < 0:
            enemigo.defensa = enemigo.defensa - self.fuerza
            print(self.nombre, "ha hecho", self.fuerza, "puntos de daño a la defensa de", enemigo.nombre)
            print("La defensa de", enemigo.nombre, "es", enemigo.defensa)
        else:
            enemigo.vida = enemigo.vida - daño
            enemigo.defensa = enemigo.defensa * 0
            if enemigo.vida < 0:
                enemigo.morir()
            print(self.nombre, "ha hecho", daño, "puntos de daño a", enemigo.nombre)
            print("Vida de", enemigo.nombre, "es", enemigo.vida)


class Guerrero(personaje):
    # Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    # Sobreescribir impresión de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("- espada:", self.espada)

    # Sobreescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

    # Escoger espada
    def escoger_navaja(self):
        opcion = int(input("Escoge la espada de energía:\n (1) Espada normal, daño 10,\n (2) Espada dañada, daño 6\n>>>> "))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 6
        else:
            print("Valor inválido, intenta de nuevo")
            # Vuelve a ejecutar el método
            self.escoger_navaja()


class Mago(personaje):
    # Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    # Sobreescribir impresión de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("- libro:", self.libro)

    # Sobreescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

    # Escoger libro
    def escoger_libro(self):
        opcion = int(input("Escoge el mejor libro:\n (1) Libro de magia negra, daño 10,\n (2) Libro normal, daño 6\n>>>> "))
        if opcion == 1:
            self.libro = 10
        elif opcion == 2:
            self.libro = 6
        else:
            print("Valor inválido, intenta de nuevo")
            # Vuelve a ejecutar el método
            self.escoger_libro()


# Crear instancias
mi_personaje = personaje("RoxGon", 20, 15, 10, 100)
arturoSuarez = Guerrero("Arutro", 20, 15, 10, 100, 5)
gandalf = Mago("gandalf", 20, 15, 10, 100, 5)

# Atributos antes de los ataques
mi_personaje.imprimir_atributos()
gandalf.imprimir_atributos()
arturoSuarez.imprimir_atributos()

# Realizar ataques
mi_personaje.atacar(arturoSuarez)
arturoSuarez.atacar(gandalf)
gandalf.atacar(mi_personaje)

# Atributos después de los ataques
mi_personaje.imprimir_atributos()
gandalf.imprimir_atributos()
arturoSuarez.imprimir_atributos()

# Variable del constructor para un enemigo
mi_enemigo = personaje("El Antagonista", 10, 50, 45, 100)

# Ataques y pruebas adicionales
# mi_personaje.atacar(mi_enemigo)
# mi_enemigo.imprimir_atributos()

# mi_personaje.subir_nivel(15, 20, 30)
# print("Valores actualizados")
# mi_personaje.imprimir_atributos()

# Modificando valores de los atributos
# mi_personaje.nombre = "Naruto"
# mi_personaje.fuerza = 200000
# mi_personaje.inteligencia = 44
# mi_personaje.defensa = 44
# mi_personaje.vida = 1

# print("El nombre de mi personaje es:", mi_personaje.nombre)
# print("La fuerza de mi personaje es:", mi_personaje.fuerza)
# print("La inteligencia de mi personaje es:", mi_personaje.inteligencia)
# print("La defensa de mi personaje es:", mi_personaje.defensa)
# print("La vida de mi personaje es:", mi_personaje.vida)
