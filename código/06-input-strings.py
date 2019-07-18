"""
¿Qué pasa si queremos recibir información del usuario?
La función 'input()' nos es de ayuda en esos casos. 
"""

nombre = input("¿cuál es tu nombre?: ")
ciudad = input("¿dónde naciste?: ")
print("Eres", nombre, "de", ciudad)

nacimiento = input("¿en qué año naciste?: ")
nacimiento = int(nacimiento)
edad = 2019 - nacimiento
print("Debes tener al rededor de %r años de edad" % edad)
