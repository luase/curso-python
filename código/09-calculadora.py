# decimos las instrucciones de operación
print("Ingresa dos números, uno por uno, y después un operador.")
print("(operadores válidos: +, -, /, *, <, >, <=, >=)")
# pedimos los dos números
x = input("número 1: ")
x = int(x)
y = input("número 2: ")
y = int(y)

# pedimos el símbolo del operador
operador = input("operador: ")

if operador == '+':
    # suma
    res = x + y
elif operador == '-':
    # resta
    res = x - y
elif operador == '*':
    # multiplicación
    res = x * y
elif operador == '/':
    # división
    res = x / y
elif operador == '<':
    # menor que
    res = x < y
elif operador == '>':
    # > mayor que
    res = x > y
elif operador == '<=':
    # <= menor o igual que
    res = x <= y
elif operador == '>=':
    # >= mayor o igual que
    res = x >= y
else:
    print("OPERADOR NO VÁLIDO!")
    res = 'ERROR'


"""
Ahora imprimimos los resultados.
"""
print("%r %s %r = %r" % (x, operador, y, res) )