# LISTAS
# Secuencias ordenadas de valores
# lista = [... , ... , ... ,]

# Podemos colocar todo tipo de valores en una lista
primos = [2, 3, 5]
planetas = ['mercurio', 'venus', 'tierra', 'neptuno']
lista1 = [1, '2', 'tres', {}]

# Incluso una Lista de listas
lista2 = [
    ['amarillo', 'verde'],
    primos,
    planetas
]
print(lista2)


# INDEXING 
# Acceso a valores de la lista mediante el indice, comenzando en 0
# O con numeros negativos, comenzando desde el final de la lista
planetas[1]  # 'venus'
planetas[-1] # 'neptuno' (ultimo de la lista)

# SLICING
# Selecciona un trozo de la lista
# [start:end] -> end, sin incluir
planetas[1:3]  # ['venus', 'tierra']

# [start:end] son OPCIONALES
# [:3] -> desde 0 hasta 3 (sin incluir)
# [1:] -> desde 1 hasta el final
planetas[1:-1] # todos menos el 0 y el ultimo


# MODIFICACION DE LISTAS
# Simplemente asignando un valor a elemento o trozo (por indice o slice)
planetas[2] = 'home'
planetas[:3] = ['merc', 'ven', 'tierr']


# FUNCIONES SOBRE LISTAS
# Propias de Python, realizan diferentes procesos sobre una lista
# - len()     - sorted()    - sum()   - max()
n_planetas = len(planetas)
planetas_ordenado = sorted(planetas)
suma = sum(primos)
max_primo = max(primos)

# OJO: Pueden arrojar error 
# si se utilizan sobre tipos de datos que no corresponden


# METODOS DE LISTAS
# Funciones propias del objeto Lista
planetas.append('pluton')   # agrega al final
planetas.pop()              # remueve (y devuelve) el ultimo elemento
planetas.index('tierra')    # indice del elemento en la lista (eeror si no existe)
'tierra' in planetas        # indica si el emento se encuentra en la lista


# TUPLAS
# Basicamente iguales a las listas
# Dos diferencias:
# 1- Se definen con parentesis, no corchetes
#    tupla = (1,2,3)
# 2- Son INMUTABLES -> NO se puede t[2] = 100

# Suelen utilizarse en funciones que retornan mulitp valores
# (asumo que por su inmutabilidad, asegura que no se modif los result)
x = 0.125
x.as_integer_ratio() # tupla (1,8)

# Puedo luego, asignar estos valores de la tupla 
# a multiples variables de manera sencilla
numerador, denominador = x.as_integer_ratio()

# Otro ejemplo donde se puede ver su uso es en el swap de variables
a = 1
b = 2
a, b = b, a
print('a:', a, 'b:', b)