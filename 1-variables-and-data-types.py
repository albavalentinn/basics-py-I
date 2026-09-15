"""
--------------------------- VARIABLES / TIPOS DE DATOS ---------------------------
En este taller aprenderás cómo crear variables, trabajar con diferentes tipos de datos.
"""

"""
--- Ejercicio 1 Variables---
Crea una variable llamada "mensaje". 
Asígnale el valor "¡Hola, Mundo!". 
Imprime el valor de la variable en la consola.
"""
message = "¡Hola, Mundo!"
print(message)

"""
--- Ejercicio 2 Variables---
Invoca la variable anterior llamada "mensaje". 
Reasígnale el valor "Hello world!". 
Imprime el valor de la variable en la consola.
Escribe en un comentario de línea lo que sucede.
"""
message = "Hello world!"
print(message)

"""
--- Ejercicio 3 Tipos de datos---
Crea variables para cada uno de los siguientes tipos de datos y colecciones: string, int, float, 
bool, list, tuple, dicctionary and set. 
Imprime cada variable y el tipo de dato o colección que almacena en la consola.
"""
user_name = "Alex"                                  # string
total_points = 100                                  # int
average_score = 9.85                                # float
is_student = True                                   # bool
programming_languages = ["Python", "JavaScript"]    # list
map_coordinates = (40.4165, -3.70256)               # tuple
user_profile = {"name": "Alex", "role": "admin"}    # dictionary
unique_ids = {101, 102, 103, 104}                   # set

# Imprimimos la variable y la función type() para mostrar el tipo de dato
print(user_name, type(user_name))
print(total_points, type(total_points))
print(average_score, type(average_score))
print(is_student, type(is_student))
print(programming_languages, type(programming_languages))
print(map_coordinates, type(map_coordinates))
print(user_profile, type(user_profile))
print(unique_ids, type(unique_ids))
