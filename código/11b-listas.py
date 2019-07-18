# Pertenencia, o como usar operadores lógicos con
# listas

# tenemos una lista con usuarios permitidos
usuarios_permitidos = ['root', 'jaime', 'saul']
# y tenemos un login
usuario = input("Ingresa tu nombre de usuario> ")
# revisamos si el usuario pertenece o no a la lista
if usuario in usuarios_permitidos:
    print('Bienvenido', usuario)
else:
    print('El usuario', usuario, "no es un usuario permitido")

# lo mismo, pero con un pin (contraseña)
# lista de usuarios
usuarios = [    
    ['alberto',  '1234'],
    ['cutberto', '4242'],
    ['gilberto',   '7524'],
    ['humberto',   '9843']
]
# pedimos un usuario
username = input('Nombre de usuario: ')
# pedimos una contraseña
pin = input('código PIN: ')
# revisamos esta combinación
if [username, pin] in usuarios:
    print('Bienvenido', username)
else:
    print("ERROR de contraseña y/o usuario")