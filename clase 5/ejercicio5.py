
"""
-ingresar el registro de cada mes : Usando un bucle while para solicitarlo. 
-Validar que los ingresos sean números positivos. 
-Si se ingresa un valor negativo, mostrá un mensaje indicando que el valor no es válido
-volvé a pedir el dato.

"""

indice = 0
mes = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]
ingresos = int(input(f"Ingrese el registro de ingresos para el mes de {mes[indice]}: "))
suma = 0


while indice < len(mes):
    if ingresos < 0:
        print("El valor ingresado no es válido. Por favor, ingrese un número positivo.")
        ingresos = int(input(f"Ingrese el registro de ingresos para el mes de {mes[indice]}: "))
    else:
        print(f"Registro de ingresos para {mes[indice]}: {ingresos}")
        indice += 1
        if indice < len(mes):
            ingresos = int(input(f"Ingrese el registro de ingresos para el mes de {mes[indice]}: "))
            suma += ingresos
            promedio = suma / 6 
print(f"La suma de los ingresos mensuales es: {suma} y el promedio es: {promedio}")

