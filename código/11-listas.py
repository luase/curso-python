# hemos estado trabajando con secuencias todo este tiempo,
# los strings son secuencias de letras/caracteres
nombre = 'Jaime'
print(nombre[0])
print(nombre[1])
print(nombre[2])
print(nombre[3])
print(nombre[4])
# no estamos limitados a usar indices positivos
# si queremos accesar el último elemento de la 
# lista podemos usar el índice -1
print(nombre[-1])
print(nombre[-2])
print(nombre[-3])
print(nombre[-4])
print(nombre[-5])

# sin embargo, hay listas más interesantes que las de 
# caracteres en este caso tenemos una lista de strings
autores = ['Borges', 'García Márquez', 'Rulfo']
# podemos accesar a cada elemento
print(autores[0][0])
print(autores[1])
print(autores[2])
# o a la lista entera
print(autores)

# como mencionaba, las listas pueden contener distintos
# tipos de variables
jaime = ['Jaime Alonso', 23, "Castaño", True]
print(jaime)

# una lista puede contener otras listas
jaime = ['Jaime Alonso', 23, "Castaño", True]
tony  = ['Tony Montana', 28, "Negro", False]
empleados = [jaime, tony]
print(empleados)
# Para accesar información especifica, usamos índices
print(empleados[0][1])

# podemos sumar listas
numeros_1_5 = [1, 2, 3, 4, 5]
numeros_6_10 = [6, 7, 8, 9, 10]
numeros = numeros_1_5 + numeros_6_10
print(numeros)

# también podemos multiplicar las listas
hola_x5 = 'hola' * 5
print(hola_x5)

# Podemos crear una lista sin elementos
lista_vacia = []
# También podemos crear una lista con n cantidad
# de 'cajones' vacios
lista_n = [None] * 10
print(lista_vacia)