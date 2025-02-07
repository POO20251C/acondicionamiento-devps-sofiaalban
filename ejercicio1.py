#Ejercicio 1
#Sofía Albán
"""
**Descripción:**  
Dado un número entero, calcula la suma de todos sus dígitos.

**Entrada:**  
- Una línea que contenga un número entero.

**Salida:**  
- Un entero que es la suma de los dígitos.

**Ejemplo de entrada:**
1234
**Ejemplo de salida:**
10

**Pistas:**  
- Puedes convertir el número a cadena para iterar sobre cada carácter o usar operaciones aritméticas (módulo y división).
"""
def numero_entero():
    suma = 0
    num_str = input("Ingrese un número entero: ") 

    for caracter in num_str:
        carc_int = int(caracter)  
        suma += carc_int  

    print(f"La suma de sus números es: {suma}")  

numero_entero()
