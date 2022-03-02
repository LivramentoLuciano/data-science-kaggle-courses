# FOR
# itera sobre un conjunto de valores y ejecuta la porcion de codigo definida dentro
# otorgando en cada iteración, el valor a una variable que definimos en el lazo
#
# for valor in rango_valores :
#    # codigo del loop
planetas = ['mercurio', 'venus', 'tierra', 'neptuno']
for planeta in planetas:
    print('Planeta:', planeta)

# el objeto de iteracion puede ser cualquiera que soporte dicha funcion
# - lista
# - tupla
# - string
mensaje = 'mi vieja mula'
for caracter in mensaje:
    print('imprimo el caracter:', caracter)

# range()
# entrega un set de valores, sobre los cuales podemos, por ej, iterar
range(5)    # 0,1,...4
for n in range(5):
    print('iteracion n*:', n)


# WHILE
# itera y repite el codigo hasta que se cumpla determinada condicion
# while condicion:
#     # codigo del loop
while i<10:
    print(i)
    i+=1


# LIST COMPREHENSION
# Funcionalidad importante de python
# Permite construir listas de manera muy concisa y entendible
#
# Ejemplo, se utiliza un for y en cada iteracion se carga un valor a la lista
cuadrados = [n**2 for n in range(10)]

# tambien, puede incluirse un condicional
short_planets = [planet for planet in planets if len(planet) < 6]

# Esta funcionalidad, combinada con funciones como min, max, sum
# puede brindarnos soluciones muy simples a problemas que requririan
# muchas lineas de codigo 
#
# Ejemplo, sin list_comprehension
def count_negatives(nums):
    count = 0
    for n in nums:
        if n < 0:
            count += 1
    return count_negatives

# con list_comprehension
def count_negatives_simple(nums):
    return len([n for n in nums if n < 0])
    # return sum([n<0 for n in nums])   # usando suma de booleanos


# Regla a la hora de codear
# Crear el codigo LEGIBLE, mas CONCISO
# Priorizar su entendimiento