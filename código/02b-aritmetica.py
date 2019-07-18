# Más operadores...
"""
Por cada operador que estamos probando imprimimos
dos veces el resultado, en el primer 'print()' hacemos
la operación dentro de los argumentos de formato,
para el segundo 'print()' calculamos el resultado
primero, lo guardamos en una variable y después
imprimimos dicha variable.
"""

# potencia
numero = 2
potencia = 3
res = numero ** potencia
print("%r^%r = %r" % (numero, potencia, numero ** potencia ) )
print("%r^%r = %r" % (numero, potencia, res ) )

# raices
numero = 16
raiz = 2
res = numero ** (1/raiz)
print("raíz %r de %r = %r" % (raiz, numero, numero ** (1/raiz) ) )
print("raíz %r de %r = %r" % (raiz, numero, res ) )

# división entera
dividendo = 33
divisor = 2
res = dividendo // divisor
print("%r//%r = %r" % (dividendo, divisor, dividendo//divisor ) )
print("%r//%r = %r" % (dividendo, divisor, res ) )

residuo = dividendo % divisor
print (residuo)