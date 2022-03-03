# STRINGS
# ya vi bastante de esto anteriormente, vamos con algunas otras cosas

# Triple comilla
# permite escribir varias lineas
mensaje_largo = '''- "Hola", le dije
- "Cómo estás?" Respondió
'''
print(mensaje_largo)

# Un string es una secuencia
# Podemos aplicarle casi todo lo que aplicamos sobre listas
# -index    -slice     -len    -loop
mensaje_largo[0]
mensaje_largo[4:10]
len(mensaje_largo)
[char + '!' for char in mensaje_largo]

# La diferencia IMPORTANTE con las listas es que SON INMUTABLES
# No podemos hacer, p/ej
# mensaje_largo[0] = 'X'

# Por defecto, print imprime una nueva linea (\n) al final
# puede modificarse
print('Hola', end=' - ')
print('mundo')


# String Methods
mensaje_largo.upper()           # convierte a mayuscula
mensaje_largo.lower()
# mensaje_largo.index('palabra')  # devuelve el indice de aparicion del arg -> error si no existe
mensaje_largo.startswith('- H') # True
mensaje_largo.endswith('ondio') # False (por acento)

# split (de string a lista de palabras)
# por defecto, separa cuando encuentra un 'whitespace'
palabras = mensaje_largo.split()

# pero puede indicarse otro separador
dateStr = '1992-10-28'
anio, mes, dia = dateStr.split('-')

# join (de lista a string)
# utilizando el String sobre el que fue llamado como separador
fecha = '/'.join([dia, mes, anio])


# Concatenacion y Format
# podemos concantear utilizando el operador +
# Ojo, si el objeto no es string, debemos covnertirlo con str()
mensaje_largo = mensaje_largo + '\n Y eso fue todo'
datetimeStr = dateStr + str(00)

# Concatenar muchos Strings (p7ej para imprimir un mensaje)
# puede volverse muy engorroso a la vista
#
# Para ello utilizamos format() y el placeholder {}
# No require usar str(), format se encarga de resolverlo
'{}, siempre seras el planeta n° {}'.format('Tierra', 3)

# Además, podemos indicar el formato en que queremos se imprima
planet = 'Pluto'
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
    ))

# dentro del corchete se puede colocar el indice de la variable correspondiente
print('{0} es {1}, {1} es {0}'.format('Hola', 'Ciao'))


