"""
Este programa nos asiste en la creación de cartas.
"""
saludo_1 = "Buenos días,"
saludo_2 = "Buenas tardes,"
nombre_1 = "Jaime Alonso"
nombre_2 = "Saúl Sánchez"
inicio = "Espero que este mensaje lo encuentre bien de salud."
cuerpo = "Le escribo esta carta para"
mensaje_1 = "recomendarle esta película: Spiderman"
mensaje_2 = "recomendarle este libro: El Aleph de Borges"
mensaje_3 = "recomendarle esta canción: and I love her - the beatles"
despedida = "Sin más por el momento"
firma = "- anónimo"

carta_titulo = saludo_2 + ' ' + nombre_1 + '\n'
carta_cuerpo = inicio + '\n' + cuerpo + ' ' + mensaje_2 + '\n'
carta_despedida = despedida + '\n' + firma

carta = carta_titulo + carta_cuerpo + carta_despedida

print(carta)
