#Ejercicio2
#Sofia Albán 
""""
## Ejercicio 2: Contar Vocales en una Cadena

**Descripción:**  
Dada una cadena de texto, cuenta el número de vocales (a, e, i, o, u, sin distinguir mayúsculas de minúsculas) que contiene.

**Entrada:**  
- Una línea de texto.

**Salida:**  
- Un entero que representa la cantidad de vocales encontradas.

**Ejemplo de entrada:**
Hola Mundo
**Ejemplo de salida:**
4
**Pistas:**  
- Recorre la cadena carácter por carácter y compara con las vocales.
- Convierte la cadena a minúsculas para simplificar la comparación.

---
"""
def vocales():
    suma=0
    frase = input("Ingrese una cadena de texto: ").lower()

    for caracter in frase:
        if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u" :
            suma+= 1
        else:
            suma+=0
        
    print(f"El número de vocales en esta cadena de texto es: {suma}")  

vocales()
