"""
Como recibir números del usuario
"""
x_string = input("base: ")
y_string = input("potencia: ")

x = int(x_string)
y = int(y_string)

print("%r elevado a la %r potencia es igual a: %r" % (x, y, x ** y))