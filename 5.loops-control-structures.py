"""
--------------------------- CICLOS Y ESTRUCTURAS DE CONTROL ---------------------------
En este taller aprenderás usar los métodos más típicos para dirigir el flujo de ejecuón y la lógica de un algoritmo
"""

"""
--- Ejercicio 1 condicionales  ---
Escribe un programa que pida al usuario una letra y luego imprima un mensaje indicando si es una vocal o una consonante.
"""
letra = input("Introduce una letra: ").lower()

if letra in "aeiouáéíóú":
    print("Es una vocal.")
else:
    print("Es una consonante.")


"""
--- Ejercicio 2  condicionales anidados  ---
Escribe un programa que pida al usuario una nota (entre 0 y 100) y determine si 
es una calificación de "A", "B", "C", "D" o "F".
"""
nota_str = input("Introduce una nota (entre 0 y 100): ")
nota = int(nota_str)

if nota >= 90:
    print("Calificación: A")
elif nota >= 80:
    print("Calificación: B")
elif nota >= 70:
    print("Calificación: C")
elif nota >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")

"""
--- Ejercicio 3  bucle while  ---
Escribe un programa que pida al usuario un número entero positivo y 
luego imprima la cuenta regresiva desde ese número hasta 1.
"""
numero_str = input("Introduce un número entero positivo para la cuenta regresiva: ")
numero = int(numero_str)

while numero >= 1:
    print(numero)
    numero -= 1

"""
--- Ejercicio 4  bucle for  ---
Escribe un programa que imprima todos los caracteres de una cadena de texto ingresada por el usuario.
"""
texto = input("Introduce una cadena de texto: ")

for caracter in texto:
    print(caracter)

"""
--- Ejercicio 5  bucle for con range ---
Escribe un programa que imprima la tabla de multiplicar del 5 (del 1 al 10).
"""
print("Tabla de multiplicar del 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

"""
--- Ejercicio 6  bucle for con listas ---
Escribe un programa que pida al usuario 5 palabras, las guarde en una lista y 
luego en una nueva lista guarde todas las palabras en mayúsculas.
"""
palabras = []

for i in range(5):
    palabra_nueva = input(f"Introduce la palabra {i + 1}: ")
    palabras.append(palabra_nueva)

palabras_mayusculas = []
for p in palabras:
    palabras_mayusculas.append(p.upper())

print("Lista original:", palabras)
print("Lista en mayúsculas:", palabras_mayusculas)


"""
--- Ejercicio 7  break and continue ---
Escribe un programa que le pida al usuario una mascota y 
si es un perro, que imprima en la consola "Tengo un perro", 
si es un gato, que imprima en la consola "Tengo un gato", 
si es un pájaro, que imprima en la consola "Tengo un pájaro" y 
si no es ninguno de los 3 que imprima "No tengo una mascota convencional"
"""
while True:
    mascota = input("Introduce una mascota: ").lower()
    
    if mascota == "perro":
        print("Tengo un perro")
        break
    elif mascota == "gato":
        print("Tengo un gato")
        break
    elif mascota == "pájaro" or mascota == "pajaro":
        print("Tengo un pájaro")
        break
    else:
        print("No tengo una mascota convencional")
        continue # Vuelve al inicio del bucle para volver a preguntar
