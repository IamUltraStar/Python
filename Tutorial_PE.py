# Librerias/Módulos
import math # Importa el modulo
from os import system # Importa una o mas funciones en especifico de un módulo

# Variables
var_int = 4 # Entero
var_float = 4.5 # Flotante
var_complex = 4.5 + 5j # Complejo
var_string = "Hello World!" # Cadena
var_bool = True # Booleano

# Colecciones
var_list = [4, 4.5, 4.5+5j, "Hello World!", True, ["a","b"], {"a":"b"}] # Lista
var_tuple = (4, 4.5, 4.5+5j, "Hello World!", True) # Tupla
var_set = set() # Conjunto vacío
var_set_1 = {4, 4.5, 4.5+5j, "Hello World!", True} # Conjunto
var_dictionary = {4:"int", "Hello World!":"string", True:"bool","list":[]} # Diccionario

# Matriz
var_matriz = [[1,2,3],
              [4,5,6],
              [7,8,9]]

# Entrada y Salida de datos
print("Hello World!") # Impresion simple en consola
print("Hello "+"World!") # Impresion simple con concatenación de cadenas
print("Variables:", var_int, var_float, var_complex, var_string, var_bool) # Imprimir cadenas y variables
print(f"Variables: {var_int} {var_float} {var_complex} {var_string} {var_bool}") # Imprimir cadenas y variables
print(f"Text", end="") # Omite el salto de linea
in_int = int(input("\nEnter a Integer: ")) # int
in_float = float(input("Enter a Float: ")) # float
in_complex = complex(input("Enter a Complex: ")) # complex
in_string = input("Enter a String: ") # string

# Sentencias Condicionales
if ():
    print("Action")
elif ():
    print("Action")
else:
    print("Action")

# Bucles
while ():
    print("Action")

for i in var_string:
    print("Action")

for i in range(var_int):
    print("Action")

# Función zip()
for item1, item2 in zip(var_list, var_tuple):
    print(f" {item1} - {item2}")

# Función enumerate()
for position,element in enumerate(var_list):
    print(f"In position {position} is the element: {element}")

# Recorrer un diccionario
for key,value in var_dictionary.items():
    print(f"{key} : {value}")

# Operador Ternario
var_string = "How are you?" if var_int > 18 else "Hello World!" # Pertenece a las setencias condicionales

# Expresión de Comprensión
var_dictionary_1 = { key:nombre for key, nombre in var_dictionary} # Genera un diccionario a partir de otro diccionario de acuerdo a la expresión

# Función lambda
function_sum = lambda x : sum(x) # Se utiliza para procesos pequeños
function_filter_par = lambda x : x % 2 == 0

# Función
def new_function(a, b = 4): # En caso no llegue un argumento a b se tomara el valor dado
    """
        The `new_function` in Python takes two arguments, with a default value of 4 for the second argument,
        and returns the sum of the two arguments while setting a global variable `var_int` to 6.
        
        :param a: The parameter `a` in the `new_function` is the first required argument that the function
        expects to receive when it is called
        :param b: The parameter `b` in the `new_function` has a default value of 4. This means that if no
        argument is passed for `b` when calling the function, it will automatically take the value of 4,
        defaults to 4 (optional)
        :return: The function `new_function` is returning the sum of the two input arguments `a` and `b`. If
        the `b` argument is not provided when calling the function, it will default to the value 4.
    """
    global var_int # Se indica que se va a trabajar con una variable global
    print("Instruction:")
    var_int = 6
    return a + b

var_int = new_function(b = 5, a = 4) # Argumento Posicional
var_int = new_function(a = 5) # Argumento unico
help(new_function) # Imprime la documentación de una función
function_reference = new_function

# Función - *args (Tupla)
def function_variables(*variables): # Se usa en caso quieras mandar muchos argumentos en un solo parámetro
    var_list = list(variables) # Se convierte en lista la tupla generada
    print(var_list)

function_variables("a", "e", "i", "o", "u")

# Función - **kwargs (Diccionario)
def function_variables_(**variables): # Se usa en caso quieras mandar muchos argumentos en un solo parámetro
    for key,value in variables.items() : #Se recorre el diccionario generado
        print(f"Key: {key}, Value: {value}")

function_variables_(name = "Clark", edad = 18)

# Funcíon - *args y **kwargs
def function_args_kwargs(*var1,**var2): # En esta función se esta trabajando con los dos tipos de argumentos(args y kwargs)
    print(f"args(tuple): {var1}")
    print(f"kwargs(dictionary): {var2}")

function_args_kwargs("a", "b", "c", id = 1, codigo = 1234)

# Funciones de Orden Superior
def squared(n):
    return math.pow(n, 2)

def cubed(n):
    return math.pow(n, 3)

def execute_action(function, value): # Consiste en pasar como argumento funciones
    return function(value)

print(execute_action(cubed, 4))

# Recursividad
def number(n): # En este caso hacemos el llamado de la función dentro de la misma función
    if(n != 0) :
        print(n)
        number(n - 1)

number(10)

# Excepción (try-except)
try:
    print(1 / 0)
except (Exception) as e:
    print(f"Error: {e}")

# Funciones de orden superior
var_list = list(map(function_sum, var_list)) # Se aplica un método o fúncion a cada elemento de un objeto iterable mutable
var_list = list(filter(function_filter_par, var_list)) # Se filtra los elementos que cumplan con la función
var_list = sorted(var_list, key = lambda x : x[0]) # Se ordena los elementos de acuerdo al elemento retornado de la función

# Métodos - String
var_substr = var_string[0: 5] # Generar una subcadena
length_string = len(var_string) # Determina la cantidad de caracteres de una cadena
var_string = var_string.strip(" ") # Elimina el primer y ultimo caracter especificado
var_string = var_string.lstrip(" ") # Elimina el primer caracter especificado
var_string = var_string.rstrip(" ") # Elimina el ultimo caracter especificado
var_bool = var_string.istitle() # Verifica si la cadena empieza con mayuscula
var_string = var_string.title() # Modifica la cadena, aplicando un nuevo formato
var_bool = var_string.islower() # Verifica si la cadena esta en minisculas
var_string = var_string.lower() # Convierte la cadena en minisculas
var_bool = var_string.isupper() # Verifica si la cadena esta en mayusculas
var_string = var_string.upper() # Convierte la cadena en mayusculas
var_string = var_string.swapcase() # Convierte las minisculas en mayusculas y viceversa
var_string = var_string.capitalize() # Convierte el primer caracter en mayuscula y las demas en minisculas
var_string = var_string.center(15, "=") # Centra la cadena y añade el caracter especificado a los costados
var_int = var_string.count("substr") # Busca la cantidad de veces que se repite una subcadena o caracter en una cadena
var_bool = var_string.startswith("He") # Verifica si una cadena empieza con la subcadena especificada
var_bool = var_string.endswith("d!") # Verifica si una cadena termina con la subcadena especificada
var_int = var_string.find("substr") # Encuentra la posicion en la que incia la subcadena especificada

# Métodos - Listas
var_list.append("new") # Agrega un elemento al final de la lista
var_list.extend(["a", "b", "c", 4, True]) # Concatenar varios elementos o listas al final de la lista
var_list.insert(var_int, "new") # Inserta un elemento en una posicion dada
var_list.pop() # Elimina el ultimo elemento de la lista
var_list.remove("Hello World!") # Elimina el primer elemento filtrado
del var_list[var_int] # Elimina el elemento con posicion dada o eliminar la lista con [:]
var_list.clear() # Limpia por completo una lista
var_list.reverse() # Invierte una lista completa
var_list.sort() # Ordena los elementos de una lista
var_int = var_list.index("Hello World!") # Encuentra la posicion de un elemento especificado c/s rango
var_float = sum(var_list) # Suma los elementos de una lista

# Métodos - Tuplas
var_subtuple = var_tuple[0: 3] # Genera una subtupla de acuerdo a la posicion dada
var_combination = zip(var_tuple, var_list) # Combina ambos elementos iterables, generando tuplas por cada posición

# Métodos - Conjuntos
var_bool = var_set_1.issubset(var_set) # Verifica si un conjuntos es subconjunto de otro conjunto
var_bool = var_set.issuperset(var_set_1) # Verifica si un conjuntos es superconjunto de otro conjunto
var_set.add("Hello World!") # Agrega un elemento al conjunto
var_set.update(var_list) # Agrega los elementos de un objeto al conjunto
var_set.remove(var_string) # Elimina un elemento dado
var_set.discard(var_string) # Elimina un elemento dado y evita error de existencia
union = var_set | var_set_1 # Union de conjuntos
intersection = var_set & var_set_1 # Intersección de conjuntos
difference = var_set - var_set_1 # Diferencia de conjuntos
symmetric_difference = var_set ^ var_set_1 # Diferencia simétrica de conjuntos

# Métodos - Diccionarios
var_dictionary["New Key"] = 6 # Genera o modifica un elemento al diccionario
var_dictionary = dict.fromkeys(var_list, "Value") # Generar un diccionario mediante una lista dada
var_list = list(var_dictionary.items()) # Obtener los items del diccionario
var_list = list(var_dictionary.keys()) # Obtener las claves del diccionario
var_list = list(var_dictionary.values()) # Obtener los valores del diccionario
var_dictionary.clear() # Limpia por completo un diccionario
new_dictionary = var_dictionary.copy() # Copia los datos a otro diccionario
var_string = var_dictionary.get("New Key", "Key not found") # Obtienes un valor del diccionario y evita errores
var_dictionary.popitem() # Elimina y/o devuelve el ultimo elemento del diccionario
var_dictionary.pop("New Key", "Key not found") # Elimina (y devuelve un valor) un elemento del diccionario
var_int = var_dictionary.setdefault("New Key", 6) # Retorna el valor de una clave en caso exista de lo contrario genera un nuevo item
new_dictionary.update(var_dictionary) # Modifica o agrega nuevos items al diccionario desde otro diccionario

# EXE: Genera un ejecutable de tu archivo mediante el comando: pyinstaller --onefile {nombre_archivo}
