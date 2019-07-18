# if

x = input("ingresa un número del 1 al 100: ")
x = int(x)

if x > 100 or x < 1:
    print("número no válido")
elif x < 50:
    print("tu número es menor que 50")
elif x > 50:
    print("tu número es mayor que 50")
else:
    print("tu número es 50!")