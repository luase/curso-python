"""
Este programa nos asiste en la creación de cartas.
"""

# 0. Mensaje de bienvenida del programa
print("Este programa le asistirá con la escritura de un correo.")

# 1. Escoger el destinatario
nombre_1 = "Jaime Alonso"
nombre_2 = "Saúl Sánchez"
print("Escoja un destinatario de la lista, o ingrese uno nuevo:")
print("[1]", nombre_1)
print("[2]", nombre_2)
opcion = input("> ")
if opcion == '1':
    destinatario = nombre_1
elif opcion == '2':
    destinatario = nombre_2
else:
    destinatario = opcion

# 2. Escoger un saludo
saludo_1 = "Buenos días,"
saludo_2 = "Buenas tardes,"
saludo_3 = "Buenas noches,"
print("Escoja un saludo de la lista, o ingrese uno nuevo:")
print("[1]", saludo_1)
print("[2]", saludo_2)
print("[3]", saludo_3)
opcion = input("> ")
if opcion == '1':
    saludo = saludo_1
elif opcion == '2':
    saludo = saludo_2
elif opcion == '3':
    saludo = saludo_3
else:
    saludo = opcion

# 3. El inicio va a ser genérico
inicio = "Espero que este mensaje lo encuentre bien de salud.\nLe escribo esta carta para"

# 4. Escoger un mensaje
mensaje_1 = "recomendarle esta película: Spiderman"
mensaje_2 = "recomendarle este libro: El Aleph de Borges"
mensaje_3 = "recomendarle esta canción: and I love her - the beatles"
print("Escoja un mensaje de la lista, o ingrese uno nuevo:")
print("[1]", mensaje_1)
print("[2]", mensaje_2)
print("[3]", mensaje_3)
opcion = input("> ")
if opcion == '1':
    mensaje = mensaje_1
elif opcion == '2':
    mensaje = mensaje_2
elif opcion == '3':
    mensaje = mensaje_3
else:
    mensaje = opcion

# 5. Mostramos los mensajes de despedida prediseñados y ofrecemos
# la opción de crear uno nuevo
despedida_1 = "Sin más por el momento"
despedida_2 = "Espero su pronta respuesta"
despedida_3 = "Me gustaría oir su opinión al respecto"
print("Escoja una despedida de la lista, o ingrese una nueva:")
print("[1]", despedida_1)
print("[2]", despedida_2)
print("[3]", despedida_3)
opcion = input("> ")
if opcion == '1':
    despedida = despedida_1
elif opcion == '2':
    despedida = despedida_2
elif opcion == '3':
    despedida = despedida_3
else:
    despedida = opcion

# 6. Quien firma
firma_1 = "J. Alonso"
firma_2 = "anónimo"
firma_3 = "su admirador secreto"
print("Escoja una firma de la lista, o ingrese una nueva:")
print("[1]", firma_1)
print("[2]", firma_2)
print("[3]", firma_3)
opcion = input("> ")
if opcion == '1':
    firma = firma_1
elif opcion == '2':
    firma = firma_2
elif opcion == '3':
    firma = firma_3
else:
    firma = opcion

# 7. Unimos las partes de la carta
carta_titulo = saludo + ' ' + destinatario + '\n'
carta_cuerpo = inicio + ' ' + mensaje + '.\n'
carta_despedida = despedida + '\n' + firma
carta = carta_titulo + carta_cuerpo + carta_despedida

# 8. Mostramos la carta completa
print(carta)
