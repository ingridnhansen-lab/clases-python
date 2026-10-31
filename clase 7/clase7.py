#1.Crear una lista vacía 

ropa = []
talles = []


#2. Crear un bucle que pida al usuario que ingrese un talle de ropa 
# y lo agregue a la lista. El bucle debe continuar hasta que el usuario ingrese "salir". 




while True:
    nombre = input("Ingrese un nombre de la prenda (o escriba 'salir' para terminar): ")
    if nombre == "salir":
                break
    talle = input("Ingrese un talle de ropa numérico (o escriba 'salir' para terminar): ")
    if talle == "salir":
        break
    try:
        talle_int = int(talle)
        ropa.append(nombre)
        talles.append(talle_int)
    except ValueError:
        print("Por favor, ingrese un talle numérico válido.")
        print("Los datos ya fueron cargados correctamente")

        for i in range(len(ropa)):
            print(f"nombre : {ropa[i]} , talle: {talles[i]}")
