import re
def validacion_email(cadena):
    text = cadena 
    pattern = "^[a-z0-9]+[\._] ?[a-z0-9]+[@]\w+[.]w{2.3}$"
    if (re.search(pattern, text)) is None:
        print ("mal")
    else: 
        print("okey")
validacion_email("hola@gmail.es")