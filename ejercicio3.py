#Ejercicio 3
#Sofia Albán
"""
## Ejercicio 3: Verificar Palíndromo

**Descripción:**  
Determina si una cadena de texto es un palíndromo, es decir, se lee igual de izquierda a derecha que de derecha a izquierda.  
**Importante:** Debes ignorar espacios y diferencias entre mayúsculas y minúsculas.

**Entrada:**  
- Una línea de texto.

**Salida:**  
- Imprime `"Sí"` si la cadena es un palíndromo, o `"No"` en caso contrario.

**Ejemplo de entrada:**
anita lava la tina
**Ejemplo de salida:**
Si


**Pistas:**  
- Elimina los espacios y convierte la cadena a una forma uniforme (por ejemplo, a minúsculas) antes de comparar.
- Puedes comparar la cadena con su reverso.

---## Ejercicio 3: Verificar Palíndromo

**Descripción:**  
Determina si una cadena de texto es un palíndromo, es decir, se lee igual de izquierda a derecha que de derecha a izquierda.  
**Importante:** Debes ignorar espacios y diferencias entre mayúsculas y minúsculas.

**Entrada:**  
- Una línea de texto.

**Salida:**  
- Imprime `"Sí"` si la cadena es un palíndromo, o `"No"` en caso contrario.

**Ejemplo de entrada:**
anita lava la tina
**Ejemplo de salida:**
Si


**Pistas:**  
- Elimina los espacios y convierte la cadena a una forma uniforme (por ejemplo, a minúsculas) antes de comparar.
- Puedes comparar la cadena con su reverso.

---
"""
def palíndromo():

    frase = input("Ingrese una cadena de texto: ").lower()
    texto_a=[]
    texto_b=[]

    for caracter in frase:
        if caracter == " ":
            print("")
        else:
            texto_a.append(caracter)
            texto_b.append(caracter)

    texto_a.reverse()
    if texto_a == texto_b:
        print(f"Si es un palíndromo")
    else:
        print(f"No es un palíndromo")

        
     

palíndromo()