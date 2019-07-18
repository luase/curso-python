"""
Funciones
"""
# len(), min(), max(), sorted()
# Estas son funciones que vienen por
# default con python. Nos ayudan a manejar
# las listas.

fechas = [1996, 1990, 2019, 2000]

# len() sirve para calcular la longitud
# de una lista, se puede decir que encuentra
# el número de elementos de una lista
longitud = len(fechas)
print('len()', longitud)

# max() y min() encuentran los elementos más
# grandes y más pequeños respectivamente
maximo = max(fechas)
minimo = min(fechas)
print('max()', maximo, 'min()', minimo)

# sorted() recibe como argumento una lista
# y devuelve una lista ordenada. Es importante recalcar
# que no modifica a la lista que recibe como argumento
# sino que devuelve una lista ordenada nueva
ordenada = sorted(fechas)
reversa = ordenada[::-1]
print('sorted()', ordenada)
print('reversa sorted()', ordenada)

"""
Métodos:
"""
# un método es una función que le pertenece a
# un objeto, sea una lista, un número, un string,
# etc. Un método se utiliza así
# objeto.metodo(argumentos)
# la diferencia más grande entre un método y
# una función, es que el método afecta al objeto
# y la función no lo hace necesariamente.

# append() es un método que se usa para agregar
# un objeto al final de una lista
undostres = [1, 2, 3]
undostres.append(4)
print('append()', undostres)

# clear() este método borra los elementos de una lista.
undostres = [1, 2, 3]
undostres.clear()
print('clear', undostres)

# count() este método cuenta las veces que un elemento
# aparece dentro de una lista
numeros = ['uno', 'dos', 'dos', 'tres', 'tres', 'tres', 'cuatro', 'cuatro', 'cuatro', 'cuatro']
print("count('dos')", numeros.count('dos'))
print("count('cuatro')", numeros.count('cuatro'))
frase = ['ser', 'o', 'no', 'ser']
print('count("ser")', frase.count('ser'))
print('count("no)', frase.count('no'))

# extend() este método, similar a append(), agrega
# no solo un elemento, sino toda una lista a otra lista
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print('extend()', a)
# extend() puede parecer similar a sumar dos listas
# a + b
# sin embargo, difiere en el hecho de que extend()
# sí modifica a 'a'

# index() es un método para encontrar el primer índice
# dentro de una lista de cierto elemento.
quote = ['estaba', 'siempre', 'absorbido', 'por', 'lo', 'que', 'siempre', 'estaba']
print('index("siempre")', quote.index('siempre'))

# insert() recibe dos argumentos, un indice y un objeto.
# ingresa el elemento a la lista, en la posición que el índice
# indique.
numeros =  [1, 2, 3, 5, 6, 7]
numeros.insert(3, 'cuatro')
print("insert(3, 'cuatro')", numeros)

# split()
frase = "porque vive sólo una vida y no tiene modo de compararla con sus vidas precedentes ni de"
palabras = frase.split(sep='o')
print(palabras)
