from ast import Break
import re
from tabnanny import check 
#Tenemos que elaborar un programa que nos indique si la dirección de correo electrónico introducida es correcta
#para esto debemos comprobar 
#Que la entrada es correcta
#Que el texto introducid tiene formato de correo electrónic 
#Que el correo introducido es el correcto

#Creación de clases que sedrán las excepciones de nuestro programa
class entrada (BaseException):
    pass
class formato_email (BaseException):
    pass
class email_incorrecto (BaseException):
    pass
#Con esto podemos terminar nuestra función que comprueba el email
def check_email(cadena): #Definiremos una función que nos permita comprobar los requesitos 
    #Que la entrada es correcta
    if cadena is None or cadena == "": #Nuestra cadena no puede estar vacía
        raise entrada

    #Que el texto introducid tiene formato de correo electrónic
    text = cadena
    pattern = r"[a-z0-9-_]+[@]+[a-z]+[.]+[a-z]{2,}" 
    if (re.search(pattern, text)) is None: 
        raise formato_email

    #Que el correo introducido es el correcto
    if cadena != "vincent@eni.es":
        raise email_incorrecto

