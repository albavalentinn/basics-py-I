"""
--------------------------- MANIPULACIÓN DE STRINGS ---------------------------
En este taller aprenderás cómo crear manipular cadenas de texto y cómo manejar entradas de datos del usuario.
"""

"""
--- Ejercicio 1 ---
Crea una variable llamada "hobbie". 
Asígnale como valor una string con uno de tus hobbies". 
Crea otra variable llamada "name"
Asígnale como valor una string con tu nombre". 
Crea otra variable llamada "teammate"
Asígnale como valor una string con el nombre de una compañera". 
Crea una variable llamada "teammate-hobbie". 
Asígnale como valor una string con unos de sus hobbies". 
"""
hobby = "jugar a videojuegos"
name = "Alba"
teammate = "Lucía"
teammate_hobby = "leer novelas de misterio"

"""
--- Ejercicio 2 Concatenación ---
Imprime por consola el siguiente mensaje concatenando las variales anteriormente declaradas:
"Soy [name] y en mis tiempos libres me gusta [hobbie]"
"""
print("Soy " + name + " y en mis tiempos libres me gusta " + hobby)

"""
--- Ejercicio 3 f-strings ---
Imprime por consola el siguiente mensaje usando f-strings para unir las frases de las variales anteriormente declaradas:
"Ella es [teammate] y en sus tiempos libres le gusta [teammate-hobbie]"
"""
print(f"Ella es {teammate} y en sus tiempos libres le gusta {teammate_hobby}")
"""
--- Ejercicio 4 separación por comas ---
Imprime por consola el siguiente mensaje usando separación por comas para unir las frases de las variales anteriormente declaradas:
"Ella se llama [teammate] y yo me llamo [name]"
"""
print("Ella se llama", teammate, "y yo me llamo", name)
"""
--- Ejercicio 5 separación con operador % ---
Imprime por consola el siguiente mensaje usando separación con el operador % para unir las frases de las variales anteriormente declaradas:
"Además de programar, nos gusta [hobbie] y [teammate-hobbie]"
"""
print("Además de programar, nos gusta %s y %s" % (hobby, teammate_hobby))

"""
--- Ejercicio 6 input data ---
Escribe dos variables que reciban por terminal un número cada una
"""
first_number = input("Por favor, introduce el primer número: ")
second_number = input("Por favor, introduce el segundo número: ")
"""
--- Ejercicio 7 ---
Imprime por consola el resultado de la suma de los dos número obtenidos anteriormente y 
en un comentario de línea escribe lo que sucede. ¡Recuerda que puedes usar type() para indagar mas!
"""
print(first_number + second_number)

"""
--- Ejercicio 6 conversión de strings ---
Transforma los valores recibidos en el ejercicio 6 a números
Imprime por consola el resultado de la suma de los dos número obtenidos anteriormente
"""
first_number_int = int(first_number)
second_number_int = int(second_number)

print("El resultado de la suma matemática es:", first_number_int + second_number_int)