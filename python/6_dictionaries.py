# DICCIONARIOS
# Permiten mapear 'keys' a 'valores'
numeros = {
    'uno': 1,
    'dos': 2,
    'tres': 3
}

# Puedo acceder a sus valores indicando el valor de la 'key' entre []
# similar a un acceso via index
# tanto para lectura como escritura (si no existe, lo agrega)
numeros['dos'] # 2
numeros['once'] = 11


# DICTIONARY COMPREHENSION
# Permite crear un diccionario, de manera sencilla, como con las listas
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets_to_initials = {planet: planet[0] for planet in planets}
print(planets_to_initials)


# Operador in -> si existe ENTRE LAS KEYS
'Mercurio' in planets_to_initials


# ITERAR sobre un DICCIONARIO, lo hara sobre sus KEYS
for k in numeros:
    print('{} = {}'.format(k, numeros[k]))

# Por otro lado, podemos obtener:
#   - dict.keys()   -> lista keys
#   - dict.values() -> lista valores
' - '.join(sorted(planets_to_initials.values()))

# o bien los pares (key, value) -> item
# - dict.items()
for planet, initial in planets_to_initials.items():
    print('{} empieza con {}'.format(planet, initial))