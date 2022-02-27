# BOOLEANOS
# Tipo de datos con 2 valores posibles:
# True / False

# Operadores Booleanos 
# (comparaciones que responden SI/NO)
# - a == b      - a != b
# - a < b      - a > b
# - a <= b      - a >= b

print(3.0 == 3)    # True
print('3' == 3)    # False

# Ejemplo de aplicacion basico
def can_run_for_president(age):
    """Devuelve si alguien de determinada edad puede postularse para presidente"""
    # Segun la constitucion en USA, debes ser mayor de 35 años
    return age >= 35
print('Puede alguien de 38 años postularse?', can_run_for_president(38))

# Ejemplo de aplicacion, combinando con operacion matematica
def is_even(n):
    """Devuelve si un numero es par"""
    return (n % 2) == 0
print('Es par el numero 5? ', is_even(5))

# Combinacion de Valores Booleanos -> evaluación lógica mas compleja
# Solo requiere incorporar:
# - and         - or        - not
def can_run_for_president(age, is_natural_citizen):
    """Devuelve si alguien de determinada edad y condicion de ciudadania 
    puede postularse para presidente"""
    # Segun la constitucion en USA, debes haber nacido alli Y ser mayor de 35 años
    return is_natural_citizen and age >= 35 
print('Puede alguien de 38 años, pero no nadico en USA postularse?', can_run_for_president(38, False))

# Importante: poseen un orden de evaluacion
# P/ej: AND se resuelve antes que OR
# Se puede recordar el orden, pero PARA EVITAR ERRORES INDESEADOS
# Lo mas seguro es UTILIZAR PARÉNTESIS
# prepared_for_weather = have_umbrella or (rain_level < 5 and have_hood) or not (rain_level > 0 and is_workday)

# incluso se puede escribir en lineas separadas
# enfatizando cada parte de la evaluacion
# prepared_for_weather = (
#     have_umbrella
#     or (rain_level < 5 and have_hood)
#     or not (rain_level > 0 and is_workday)
# )


# CONDICIONALES
# if... elif... else
#
# Permiten seleccionar que código se ejecutará
# basado en cierta condicion booleana
def inspect(x):
    if x == 0:
        print('x es 0')
    elif x > 0:
        print('x positivo')
    elif x < 0:
        print('x negativo')
    else:
        print('x es algo desconocido')
    print('Esto se imprime siempre, sin importar el valor de x')

inspect(1)
inspect(-16)


# Conversion Booleana -> bool()
# Permite convertir otros tipos de datos a booleanos
# 
# En gral:
# - Numeros: siempre True, excepto el 0
# - Strings: siempre True, excepto el "" (empty)
# - List, tuplas, etc: True, excepto vacias
print(bool(25))
print(bool(0))
print(bool('sarasa'))
print(bool(''))

# se pueden utilizar en condicionales
# Python los convierte a su valor booleano implicitamente
if 0:
    print('entro al 0')
elif 'sarasa':
    print('sarasa')


# IMPORTANTE: sobre conversion booleana (y viceversa)
# - int(True) = 1
# - int(False) = 0
#
# Este concepto es muy utilizado, para obtener de manera sencilla
# mediante aritmetica conclusiones que con evaluaciones logicas serian mas complicados
# Es decir, PUEDO SUMAR VALORES BOOLEANOS
#
# Por ejemplo: deseamos saber si un sandwich posee solo 1 ingrediente (de varios)
def solo_un_ingrediente(mostaza, ketchup, pepino):
    return (int(mostaza) + int(ketchup) + int(pepino)) == 1
    # puede evitarse el 'int()' y lo convierte implicitamente
    # return (mostaza + ketchup + pepino) == 1 

print('Mi sandwich de pepino y mostaza tiene un solo ingrediente?', solo_un_ingrediente(True, False, True))
print('Mi sandwich de solo mostaza tiene un solo ingrediente?', solo_un_ingrediente(True, False, False))

# Lo anterior lo vi usar mucho en analisis de datos
# P ej, hay metodos (como is_null()) que de una lista de datos convierten a True / False
# Y luego, sobre esta puedo realizar un conteo (suma, sobre valores booleanos)
# y llegar a un resultado deseado (ejemplo: cuantas personas ingresaron una direccion valida)


# OPERADOR CONDICIONAL TERNARIO
# Permite asignar uno u otro valor basado en una condicion booleana
# de manera sencilla en una sola linea de codigo
#
# mi_dato = valor1 if condition else valor2
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    candies_msg = 'candy' if(total_candies == 1) else 'candies'
    print("Splitting", total_candies, candies_msg)
    return total_candies % 3

to_smash(91)
to_smash(1)