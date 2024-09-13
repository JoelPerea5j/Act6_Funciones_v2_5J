print("Funciones v2")
print("Perea Joel Alberto")
#Zona de Listas Tuplas set y Diccionario
celulares=["Samsung A52 ","Iphone 11 ","Chafa"]

Perros=["Chihuahuas ","Dalmata ","Pastor Aleman","PitBull","bullDog"]

Yo= {
    "Nombre":"Joel Alberto Perea Castorena",
    "Edad":16,
    "Especialidad" : "Programacion"
}

Juegos={"Metal Gear Rising ","Fifa 22 ","COD Warzone ","Geometri Dash"}




# Zona de Funciones
def verlista(Telefono):
 for Elcelular in Telefono:
        print(Elcelular)
print(" ")
def verperros(Raza):
    for Losperros in Raza:
        print(Losperros)
print(" ")
def Verjuegos(Juegitos):
    for Juegotes in Juegitos:
     print(Juegotes)

print(" ")

# Llamada a Funciones
print("Imprime los Celulares de una Lista")
verlista(celulares)

print(" ")

print("Imprime las Razas de Perros")
verperros(Perros)

print(" ")

print(Yo)
for Soy_ese in Yo:
    print(Yo[Soy_ese])

print("")
print(Juegos)
for Perea in Juegos:
    print(Perea)