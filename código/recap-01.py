"""
En el primer día del curso aprendimos bastantes
cosas, entre las más importantes está lo siguiente:
"""
# Comentarios
# Operadores
#   - Matemáticos
#   - Lógicos
# Variables
"""
Vamos a hacer un repaso de esto programando una 
calculadora básica.
"""

# Necesitamos dos números para empezar
x = 100
y = 3

"""
Comencemos con definir que operaciones vamos a incluir
Primero las operaciónes matemáticas
"""
# suma
suma = x + y
# resta
resta = x - y
# multiplicación
mult = x * y
# división
divi = x / y

"""
Ahora los operadores lógicos
"""

# < menor que
menor = x < y
# > mayor que
mayor = x > y
# <= menor o igual que
menor_igual = x <= y
# >= mayor o igual que
mayor_igual = x >= y

"""
Ahora imprimimos los resultados.
"""

# r de raw
print("Operaciones con los números %r y %r" % (x, y))
print("Suma: %r" % suma)
print("Resta: %r" % resta)
print("Multiplicación: %r" % mult)
print("División: %r" % divi)
print("%r < %r: %r" % (x, y, menor))
print("%r > %r: %r" % (x, y, mayor))
print("%r <= %r: %r" % (x, y, menor_igual))
print("%r >= %r: %r" % (x, y, mayor_igual))
