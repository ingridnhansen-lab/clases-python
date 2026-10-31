#ELIF Y MATCH

import unicodedata

def normalizar(texto):
    # Elimina acentos y convierte a minúsculas
    texto = unicodedata.normalize('NFKD', texto)
    texto = texto.encode('ASCII', 'ignore').decode('ASCII')
    return texto.lower()

#Formatee correctamente los textos ingresados en “apellido” y “nombre”, convirtiendo la primera letra de cada palabra 
# a mayúsculas y el resto en minúsculas.
#Asegure que el correo electrónico no tenga espacios y contenga solo una “@”.
#Que clasifique por rango etario basándose en su edad (“Niño/a” para los menores de 15 años, “Adolescente” de 
# 15 a 18 y “Adulto/a” para los mayores de 18 años).

#--------------------------------------------------------------------------------------------------------------

#1. Si el nombre viene en minuscula entonces, convertir primer letra a mayuscula 

nombre = input ("Ingresa tu nombre y apellido completo para comenzar") 
print(nombre.title())

#---------------------------------------------------------------------------------------------------------------

# 2. Pedir el correo electrónico:
# a.no debe tenere espacios
# b.debe contener solo una “@”.

while True:
    mail = input("Ingresa tu mail")
    if " " in mail:
        print("El mail no debe tener espacios, ingrésalo nuevamente")
    elif mail.count("@") != 1:
        print("Error: el correo debe contener solo un '@', ingrese el mail nuevamente")
    else:
        print("Mail correcto", mail)
        break

#----------------------------------------------------------------------------------------------------------------

#3. Que clasifique por rango etario basándose en su edad (“Niño/a” para los menores de 15 años, “Adolescente” de 
# 15 a 18 y “Adulto/a” para los mayores de 18 años).

#mayor = < y menor es = a >

edad = int(input("¿Qué edad tenés? "))

if edad < 0:
    print("Hay un error en tu edad:", edad)
elif edad < 15:
    print("Tu curso es para niños.")
elif edad <= 18:
    print("Tu curso es para adolescentes.")
else:
    print("Tu curso es de adultos.")

#---------------------------------------------------------------------------------------------------------------

#4. No existía en lo que se pide del ejercicio pero me quedó de la práctica 
clase = input ("¿qué clase tomás?") 

if clase == "filosofía" : print("tu aula es la número 5")
elif clase == "matemática" :print ("tu aula es la número 7")
elif clase == "biología" : print ("tu aula es la número 6")
else: print ("cursas en el aula Magna")

# - NO OLVIDARME DE LOS :
# == (IGUAL A .....)
# input = para reservar datos  