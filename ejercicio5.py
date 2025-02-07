#Ejercicio 5
#Sofia Albán
## Ejercicio 5: Contar Palabras en una Cadena
"""
**Descripción:**  
Dada una cadena de texto, cuenta la cantidad de palabras que contiene.  
Se asume que las palabras están separadas por uno o más espacios.

**Entrada:**  
- Una línea de texto.

**Salida:**  
- Un entero que indica la cantidad de palabras.

**Ejemplo de entrada:**
Hola mundo desde Python
**Ejemplo de salida:**
4


**Pistas:**  
- Utiliza el método `split()` para dividir la cadena en palabras.

---
"""

def contar_palabras():
    texto = input("Ingrese frase: ")# Leer la entrada y eliminar espacios al inicio y al final
    palabras = texto.split(" ")  # Dividir la cadena en palabras usando espacios como separadores
    print(len(palabras))  # Imprimir la cantidad de palabras

contar_palabras()
