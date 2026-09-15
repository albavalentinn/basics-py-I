"""
--------------------------- COLECCIONES ---------------------------
En este taller aprenderás a manipular coleccciones de datos: Listas, diccionarios, tuplas y sets.
"""

"""
 --- LISTAS ---
Las listas son ordenadas y mutables.
Pueden contener elementos duplicados.
Puedes modificar, añadir y eliminar elementos.
"""
"""
--- Ejercicio 1 Listas ---
Crea una variable "mascotas" que almacene una lista con los siguientes elementos: 'perro', 'gato', 'loro'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
pets = ['perro', 'gato', 'loro']
print("Lista inicial:", pets)

print("Cantidad de mascotas:", len(pets))

print("Mascota en la posición 2:", pets[2])

pets.append('teckel')
print("Lista tras añadir:", pets)

pets[1] = 'hámster'
print("Lista tras modificar la posición 1:", pets)

pets.remove('loro')
print("Lista tras eliminar 'loro':", pets)

"""
 --- TUPLAS ---
Las tuplas son ordenadas e inmutables.
Pueden contener elementos duplicados.
No puedes modificar, añadir o eliminar elementos después de la creación.
"""

"""
--- Ejercicio 2 Tuplas ---
Crea una variable "plantas" que almacene una tupla con los siguientes elementos: 'cactus', 'orquidea', 'rosas'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
plants = ('cactus', 'orquidea', 'rosas')
print("\nTupla inicial:", plants)

print("Cantidad de plantas:", len(plants))

print("Planta en la posición 2:", plants[2])

# Intentar modificar una tupla
# plantas[1] = 'hoja rota'  # Descomenta esta línea para ver qué sucede
# Análisis: Si descomentamos la línea, Python lanzará un error tipo 'TypeError'
# Esto confirma que las tuplas son inmutables: una vez creadas en la memoria, no podemos alterar sus valores.


"""
 --- SETS ---
Los sets son desordenados y mutables.
No pueden contener elementos duplicados.
Puedes añadir y eliminar elementos, pero no puedes modificar los elementos existentes.
"""

"""
--- Ejercicio 3 Sets ---
Crea una variable "nombres" que almacene un set con los siguientes elementos: 'María', 'Cris', 'Cris', 'Alex'
Imprime por la terminal dicha variable
Haz los pasos pedidos
"""
names = {'María', 'Cris', 'Cris', 'Alex'}
print("\nSet inicial:", names)

# Explica qué sucede cuándo imprimes el valor que almacena "nombres"
# Análisis: El nombre 'Cris' solo aparece una vez en la consola. Los sets eliminan automáticamente cualquier dato duplicado. 
# Además, el orden al imprimir puede variar respecto a cómo lo escribimos, porque los sets no tienen orden.

# Escribe el código para saber la cantidad de elementos que tiene el set, imprimir por consola
print("Cantidad de nombres únicos:", len(names))

# Escribe el código para acceder al valor de la posición 3, imprimir por consola
# Para acceder por posición, primero debemos convertir el set a una lista:
names_list = list(names)
# Como el set eliminó un duplicado, ahora solo hay 3 elementos (índices 0, 1, 2). 
# Accedemos a la última posición disponible (índice 2):
print("Valor en la posición 2 (tras convertir a lista):", names_list[2])

# Escribe el código para agregar una elemento al set, imprimir por consola el set
names.add('Alba')
print("Set tras añadir:", names)

# Escribe el código para eliminar un elemento del set, imprimir por consola el set
names.remove('María')
print("Set tras eliminar:", names)

"""
 --- DICCIONARIOS ---
Los diccionarios son desordenados y mutables.
Contienen pares clave-valor.
Puedes añadir, modificar y eliminar pares clave-valor.
"""

"""
--- Ejercicio 4 Diccionarios ---
Crea un diccionario llamado "ciudad" con las claves 'nombre' y 'pais' y los valores 'Barcelona' y 'España' respectivamente.
Imprime el diccionario 
"""
city = {'nombre': 'Barcelona', 'pais': 'España'}
print("\nDiccionario inicial:", city)

# Escribe el código aquí para acceder y ver por consola el valor de 'nombre'
print("El nombre de la ciudad es:", city['nombre'])

# Escribe el código aquí para añadir un nuevo par clave-valor y ver por consola el valor de 'ciudad'
city['habitantes'] = 1620000
print("Diccionario tras añadir habitantes:", city)

# Escribe el código aquí para modificar el valor de un par clave-valor de 'ciudad' y verlo por consola
city['nombre'] = 'Palencia'
print("Diccionario tras modificar el nombre:", city)

# Escribe el código aquí para eliminar un par clave-valor de 'ciudad' y verlo por consola
del city['pais']
print("Diccionario final tras eliminar el país:", city)
