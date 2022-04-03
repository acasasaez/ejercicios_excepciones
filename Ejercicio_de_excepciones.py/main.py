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
    