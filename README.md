# ejercicios_excepciones
En este capítulo del libro trabajamos las excepciones. 

Para esta tarea teníamos que elaborar un código que nos permitiese comprobar un correo electrónico concreto. 

Para esto debíamos comprobar: que la entrada del correo fuese correcta, que el correo contase con formato de correo electrónico y que el correo electrónico introducido fuese, concretamenete, el que se nos indica edn el enunciado.

Por aquí dejo el diagrama de m i ejercicio: 

  *NOTA: lo entrgo como hacíamos en el primer cuatrimestre porque no me deja autorizar el acceso a mi repositorio desde Draw.io.
  
![ejercicio excepciones](https://user-images.githubusercontent.com/91721826/161427507-810ec361-7427-4752-be6c-54b2224478ef.jpg)

Código: 

Código en el main:

```
from excepciones import*
if __name__ == "__main__":
    a = False 
while not a:
    try:
        cadena = input("Introducir correo: ")
        check_email(cadena)
    #si llegamos al Break quiere decir que nuestro código ha sido examinado y cumple los requisitos, 
    #por eso nuestro programa sale del bucle
        break
    except entrada:
        print("Entrada incorrecta")
    except formato_email:
        print ("Introduzca una dirección de correo electrónico válida. Ej: manoloperz@gmai.com")
    except email_incorrecto:
        print("Dirección de correo electrónico incorrecta. Acceso denegado")
        a = True

if not a:
    print("Bienvenido Vicente")
    
  ```
  
  Código para crear nuestras clases: 
  
  ```
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
```
