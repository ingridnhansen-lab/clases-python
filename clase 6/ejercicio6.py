#Tu tarea es la siguiente:
#Parte 1:
#Crear una lista con los nombres de los y las clientes que vamos a procesar. Recorrer la lista y mostrar el 
#nombre de cada cliente o clienta, junto con su posición en la lista (por ejemplo, Cliente 1, Cliente 2, etc.).

#Recorrer la lista con un for y mostrar el nombre de cada cliente junto con su posición en la lista 
#(por ejemplo: Cliente 1: Ana).

#Si encontrás un nombre vacío, mostrar un mensaje de alerta indicando que ese dato no es válido.

#Ejemplo de salida:

#Cliente 1: Ana
#Cliente 2: Juan
#Cliente 3: [ALERTA] Nombre no válido
#Cliente 4: Marta

clientes = ["Cliente 1: Ana","Cliente 2: Juan","","Cliente 4: Marta"]

for busqueda in clientes:
        print(busqueda)
        if busqueda == "":
            print(f"Cliente 3 = [ALERTA] Nombre no válido ")

