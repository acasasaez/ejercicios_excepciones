import re
def validacion_email(cadena):
    text = cadena 
    pattern = r"[a-z0-9-_]+[@]+[a-z]+[.]+[a-z]{2,}" #Parece que este patrón funciona para la búsqued DEL CORREO
    if (re.search(pattern, text)) is None:
        print ("mal")
    else: 
        print("okey")

#Hacemos pruebas para comprobar wue es efectivo 
print("Prueba 1 ")
validacion_email("vicenta@gmail.es")
print (" ")
print("Prueba 2")
validacion_email("vicenta@gmailes")
print(" ")
print("Prueba 3")
validacion_email("vicentagmail.es")
print(" ")
print("Prueba 4")
validacion_email("vicenta")