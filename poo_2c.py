class Personaje:
    #Atributos de la clase
    nombre = 'Default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

#Variable del constructor vacío
mi_personaje = Personaje()
#Modificando valores de los atributos
mi_personaje.nombre = "Rodrigo"
mi_personaje.fuerza = 400
mi_personaje.inteligencia = 500
mi_personaje.defensa = 1000
mi_personaje.vida =100

print("El nombre de mi personaje es: ",mi_personaje.nombre)
print("El nombre de mi personaje es: ",mi_personaje.fuerza)
print("El nombre de mi personaje es: ",mi_personaje.inteligencia)
print("El nombre de mi personaje es: ",mi_personaje.defensa)
print("El nombre de mi personaje es: ",mi_personaje.vida)