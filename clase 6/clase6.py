#variable 
materia = ["matemática","química", "física", "tecnología","biología", "aritmética"]

#for recursar in materia :
#    print(f"Esta es la materia que te toca recursar: {recursar}")

materia_exenta= "sociología"

for recursar in materia:
        if recursar == materia_exenta:
            print(f"Ir con la profesora para coordinar {recursar}")
            break
        print("buscando, aguerde unos minutos....")
        print("fin de la búsqueda")

#range solo sive para números 
for i in range(1, 11):