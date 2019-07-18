"""
'if-else'
Hay ocasiones en las que dependiendo de una
o más condiciones, queremos que nuestro código
realice o no ciertas operaciónes.
"""

print("Bienvenido al programa del clima")
temperatura = input("está haciendo calor afuera?: ")

if temperatura == 'si':
    print("debe ser verano!")
elif temperatura == 'no':
    print("debe ser invierno!")
else:
    print("creo que no te entiendo :(")
    print("Intenta de nuevo")

print("Fin del programa")