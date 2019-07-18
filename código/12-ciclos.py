"""
En esta primer parte revisamos algunas otras
propiedades que tienen ciertos operadores
que nos van a ayudar a sacar el máximo de los
cíclos
"""

# asignaciónes 'mágicas'
# podemos asignar más de una variable con un
# solo operador de asignación
x, y, z = 1, 2, 3
print(x, y, z)

# podemos utilizar esto para alternar el valor de dos variables
x, y = y, x
print(x, y, z)

# se puede utilizar con listas
numeros = [1, 2, 3]
a, b, c = numeros
print(a)

# al igual que con los índices en las secuencias, tenemos que
# respetar la cantidad de posibles valores que queremos asignar
# las siguientes dos líneas de código deben causar un error
# x, y, z = 1, 2
# x, y, z = 1, 2, 3, 4

# si solo nos interesan pocos valores de la lista, podemos hacer lo sig.
a, b, *restantes = [1, 2, 3, 4, 5]
print(restantes)
a, *medios, b = [1, 2, 3, 4, 5]
print(medios)
# al hacer esto, la variable que va precedida del asterísco siempre resulta
# siendo una lista
a, *b, c = [1, 2, 3]
print(a, b, c)

# Operadores aumentados
x = 1
# 'x += y' es igual a tener 'x = x + y'
# Se usa para sumar al valor de x el valor de y
x += 1
print(x)

# 'x -= y' es igual a tener 'x = x - y'
# Se usa para restar al valor de x el valor de y
x -= 1
print(x)

# 'x *= y' es igual a tener 'x = x * y' 
# Se usa para multiplicar el valor de x por el valor de y
x *= 10
print(x)

# 'x /= y' es igual a tener 'x = x / y' 
# Se usa para dividir el valor de x por el valor de y
x /= 5
print(x)

"""
Ciclos
"""
# ciclo 'while'
# el ciclo while realiza las operaciones dentro de él
# sin parar, hasta que se cumpla una condición
x = 1
while x <= 100:
    print(x)
    x += 1

# Con este ciclo, podemos asegurarnos de que una condición
# deba ser cumplida para continuar.
name = ''
while not name:
    name = input('Ingresa tu nombre, por favor: ')
print('Hola, %s!' %name)
 
# ciclo 'for'
# es uno de los ciclos más flexibles de python
frase = 'hola mundo, esta es la frase nueva'
frase = frase.split(sep=' ')
for elemento in frase:
    print(elemento)

# [
#     [cosa1, cosa2],
#     [cosa3, cosa 4]
# ]
# x, y = [cosa1, cosa2]
# en ocasiones necesitamos el índice
for i, elemento in enumerate(frase):
    print('[%d] - %s' % (i, elemento))

# estilo C o C++
rango = list(range(0, len(frase)))
longitud = len(frase)
rango_2 = range(0, longitud)
indices = list(rango_2)
ind_rev = indices[::-1]
# [0, 1, 2, ..., len(frase)]
for i in ind_rev:
    print(frase[i])

# Si queremos hacer un ciclo n número de veces, sin una lista
# range(x, y) nos regresa un objeto tipo rango
# list(range(x, y)) la función list() nos devuelve una lista 
# con los argumentos que ingresemos, si ponemos un rango
# nos devuelve una lista de número dentro de ese rango

for i in list(range(0, 10)):
    print(i)
