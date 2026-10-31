productos = {}

nombre= input ("nombre del producto (o 'salir' para terminar):").lower()
while nombre != "salir":
     precio = float (input(f"precio del {}"))

     while true:
          nombre = input("nombre del producto (o 'salirpara terminar):").lower().strip()
          precio = float(input(f"precio del {}"))

          if nombre == "salir:"
            break 