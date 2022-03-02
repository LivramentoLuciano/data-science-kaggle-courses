# Esto es un comentario

# ASIGNACION DE VARIABLES
# - NO requiere declarar la variable previamente
# - NO requiere indicar el tipo de dato que va a referir
#   (Incluso podriamos, luego, asignarle un dato completamente distinto)
spam_amount = 0

# LLAMADA A UNA FUNCION
# En este caso 'print' -> funcion nativa
# imprime en pantalla lo indicado entre parentesis
print(spam_amount)

spam_amount =  spam_amount + 4

# BLOQUES DE CODIGO (condicional, se vera luego)
# IMPORTANTE: 
# Python utiliza reglas de INDENTACION para definir los bloques de codigo
# Todo el codigo que este en el mismo nivel de indentacion correspondera al mismo bloque
# en este caso, solo el 'print' se encuentra dentro del bloque 'if'
#
# El inicio del BLOQUE DE CODIGO se indica con ':' (dos puntos)
if spam_amount > 0:
    print('BUT i don\'t want any spam')

# STRINGS: 
# Puede usarse comilla simple '...' o doble "..."
# Usar uno u otro permite incluir comillas dentro 
# sin necesidad de recurrir al caracter especial \
mensaje = 'BUT i don\'t want any spam'
mensaje = "BUT i don't want any spam"
mensaje = 'Este es un string con comillas "" dentro'

viking_son = 'SPAM' * spam_amount
print(viking_son)