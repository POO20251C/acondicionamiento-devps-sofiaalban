#Ejercicio 6
#Sofia Albán
"""
## Ejercicio 6: Encontrar el Máximo y Mínimo

**Descripción:**  
Dada una lista de números enteros separados por espacios, determina cuál es el número mayor y cuál es el menor.

**Entrada:**  
- Una línea con números enteros separados por espacios.

**Salida:**  
- Dos enteros separados por un espacio: primero el número máximo y luego el mínimo.

**Ejemplo de entrada:**
3 1 4 1 5 9
**Ejemplo de salida:**
9 1


**Pistas:**  
- Puedes usar las funciones integradas `max()` y `min()` de Python.
"""
def max_min():
    texto = input("Ingrese números separados por espacios: ")  
    palabras = texto.split(" ")  
    for i in range(len(palabras)):
        palabras[i] = int(palabras[i])  
    
    maximo = palabras[0]
    minimo = palabras[0]

    for num in palabras:
        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num

    print(f" El número mayor es {maximo} , y el número menor es {minimo}")

max_min()

