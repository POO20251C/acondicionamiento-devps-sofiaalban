#Ejercicio4
#Sofia Albán 
"""
## Ejercicio 4: Invertir una Lista de Números

**Descripción:**  
Dada una lista de números enteros separados por espacios, invierte el orden de los elementos y muestra la lista invertida en una sola línea.

**Entrada:**  
- Una línea con números enteros separados por espacios.

**Salida:**  
- Una línea con los números en orden inverso, separados por espacios.

**Ejemplo de entrada:**
1 2 3 4 5
**Ejemplo de salida:**
5 4 3 2 1


**Pistas:**  
- Puedes utilizar la técnica de slicing (`lista[::-1]`) o el método `reverse()`.

---
"""
def inv():

    numero = input("Ingrese números separados por espacios: ")
    invertir=[]

    for i in numero:
        invertir.append(i)
    

    invertir.reverse()
    final = " ".join(invertir)
    print(final)

inv()