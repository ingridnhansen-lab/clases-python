#ELIF Y MATCH

import unicodedata

def normalizar(texto):
    # Elimina acentos y convierte a minúsculas
    texto = unicodedata.normalize('NFKD', texto)
    texto = texto.encode('ASCII', 'ignore').decode('ASCII')
    return texto.lower()

clase = input ("¿qué clase tomás?") 

if clase == "filosofía" : print("tu aula es la número 5")
elif clase == "matemática" :print ("tu aula es la número 7")
elif clase == "biología" : print ("tu aula es la número 6")
else: print ("cursas en el aula Magna")

# - NO OLVIDARME DE LOS :
# == (IGUAL A .....)
# input = para reservar datos  