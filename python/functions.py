# DEFINCION DE UNA FUNCION
# Se utiliza la keyword 'def' acompañada del nombre de la funcion
# Mediante ':' se indica el comienzo del bloque de codigo
# Con INDENTACION, se determina las lineas de codigo que pertenecen al bloque
# Finalmente, 'return' devolvera el valor deseado y pondra fin a la funcion
def least_difference(a, b, c):
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    return min(diff1, diff2, diff3)

print('La menor diferencia entre 5, 10 y 2 es:', least_difference(5,10,2))


# HELP y DOCSTRING
# En ocasiones, la finalidad de una funcion es clara
# No obstante, se puede utilizar el metodo built-in 'help'
# y obtener asi una descripcion de la misma
#
# Para ello, es necesario declarar un 'DOCSTRING' dentro de la funcion
# mediante un String (triple comilla, nos permite escribir varios renglones)
# debajo del 'header' de la funcion
#
# Se acostumbra en el DOCSTRING brindar tambien un ejemplo de aplicacion
# y se coloca  ">>>" para simular una ejecucion en la terminal
def most_difference(a, b, c):
    """
    Devuelve la maxima diferencia entre 2 numeros, dentro de a, b y c

    >>> most_difference(5,1,10)
    5
    """
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    return max(diff1, diff2, diff3)

print(help(most_difference))


# FUNCIONES SIN RETURN
# Es posible tmb tener funciones que no retornen ningun valor
# Como los casos built-in de 'print' o 'help' que solo imprimen en pantalla
# Este tipo de funciones devuelve un valor especial 'None' (simil a null)


# PARAMETROS POR DEFECTO
# Es posible tener ARGUMENTOS OPCIONALES con un determinado VALOR POR DEFECTO
def saludar(who='Juan', who2='carlos'):
    print('Buenas', who)
    print('Ciao', who2)

# Si no indicamos el valor del parametro, toma el valor por defecto
saludar()
saludar(who='Jose')

# Probando cosas:
# Si no colocamos el nombre del parametro, debemos respetar POSICION
# Si colocamos el nombre, podemos ubicarlo como queramos
saludar('Jose', who2='Pedro')
saludar(who2='Pedro', who='Jose')


# FUNCIONES COMO PARAMETRO
# Es posible pasar funciones como argumento de otras
def squared_call(fn, arg):
    return fn(fn(arg))

def mult_5(x):
    return 5 * x

print(squared_call(mult_5, 1))
