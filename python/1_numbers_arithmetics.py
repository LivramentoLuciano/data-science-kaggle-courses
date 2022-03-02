# NUMEROS Y ARITMETICAS
a = 50
b = 4.5

# Type -> Devuelve el tipo de dato contenido en la variable
print('La variable "a" es: ', type(a))
print('La variable "b" es: ', type(b))


# OPERACIONES ARITMETICAS
# comunes
suma = a + b
resta = a - b
multiplicacion = a * b
division_true = a / b       # siempre float
cociente_entero = a // b    # entero
resto = a % b
potencia = a ** b
negado = -a

print('Resultados:')
print('Suma: ', suma, 'Resta: ', resta, 'Multip: ', multiplicacion,  'Division: ', division_true)
print('Cociente Entero: ', cociente_entero, 'Resto: ', resto, 'Potencia: ', potencia,  'Negado: ', negado)


# Orden de las operaciones
# PEMDAS: Parentesis/Exponentes/MultDiv/AdicSubs
pi = 3.14159
radius = 10
area = pi * radius ** 2
print(area)