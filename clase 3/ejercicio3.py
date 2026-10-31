#Ejercicio práctico 
#Solicite al cliente o clienta su nombre, apellido, edad y correo electrónico.
#Compruebe que el nombre, el apellido y el correo no estén en blanco (condición &), y que la edad sea mayor a 18 años.
#Muestre los datos por la terminal, en el orden que se ingresaron. Si alguno de los datos ingresados no cumple los requisitos,
# sólo mostrar el texto “ERROR!”.

#todos los campos tienen que tener al menos un caracter y debe ser mayor de 18 años (todo se debe cumplimentar)
edad= int(input("¿qué edad tenés?"))
if edad >= 18 :
    print("eres mayor de edad, puede acceder")
else: 
    print("eres menor de edad, no puedes continuar")
    exit("Muchas gracias por tu participación")


nombre= input("¿cúal es tu nombre?")
apellido=input("¿cúal es tu apellido?")
email= input("Necesito que ingreses tu e-mail")

if nombre != "" and apellido != "" and email != "" :
    print("Muchas gracias tus datos fueron completados")
else:
    print("Tenés datos sin completar") 