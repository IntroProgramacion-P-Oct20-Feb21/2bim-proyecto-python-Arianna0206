"""
    Proyecto Bimestral
    Segundo Bimestre
    
    Problemática:
"""
"""
    Que permita ingresar nuevas cuentas de diversas plataformas.
    Las plataformas son:

    Facebook (se necesita los siguientes datos: nombre de usuario,
    edad, ciudad, pais, correo electrónico)
    Twitter (se necesita los siguientes datos: nombre de usuario,
    nombres, apellidos, edad, ciudad, pais, idioma, correo electrónico)
    Whatsapp (se necesita los siguientes datos: nombre de usuario,
    número de teléfono, edad, ciudad, pais)
    Telegram (se necesita los siguientes datos: nombre de usuario,
    número de teléfono, ciudad, pais, área de interés)
    Signal (se necesita los siguientes datos: nombre de usuario,
    número de teléfono, ciudad, pais, hobby principal)
    Instagram (se necesita los siguientes datos: nombre de usuario,
    ciudad, edad, correo electrónico)
    Flickr (se necesita los siguientes datos: nombre de usuario,
    correo electrónico)
    La aplicación debe tener los siguientes procedimientos:

    método principal - main
    método crearFacebook - (método que devuelve un valor)
    método crearTwitter - (método que no devuelve un valor)
    método crearWhatsapp - - (método que devuelve un valor)
    método crearTelegram - (método que no devuelve un valor)
    método crearSignal- (método que devuelve un valor)
    método crearInstagram - (método que no devuelve un valor)
    método crearFlickr - (método que devuelve un valor)
    En la función principal se presenta un ciclo repetitivo que
    presenta un menú de opciones:

    Si se ingresa 1 se llamará a crearFacebook
    Si se ingresa 2 se llamará a crearTwitter
    Si se ingresa 3 se llamará a crearWhatsapp
    Si se ingresa 4 se llamará a crearTelegram
    Si se ingresa 5 se llamará a crearSignal
    Si se ingresa 6 se llamará a crearInstagram
    Si se ingresa 7 se llamará a crearFlickr
    
    En cada iteración del ciclo; se pregunta al usuario si se desea salir
    del ciclo.
    
    Cada método que no devuelva valores debe imprimir un resumen de la
    cuenta creada con todos los valores ingresados

    Cada método que devuelva valores debe hacer un return con un resumen de la
    cuenta creada con todos los valores ingresados

    Cuando el usuario termina el ciclo repetitivo se debe presentar un mensaje
    con base al número total de cuentas creadas. Se debe usar el número total
    de cuentas como argumento (entero) de una función llamada obtenerMensaje

    En la función obtenerMensaje existe un parámetro. El mensaje se forma de
    la siguiente manera:
    Se usa el siguiente arreglo unidimensional:  

    (mensajeFinal(3),x(300)[{a-z}, {A-Z}, {BS}])

    Los datos asignados al arreglo son:

    mensajeFinal <-- {"Campaña con poca afluencia", "Campaña moderada
    siga adelante", "Excelente campaña"}
    
    a. Si el número de cuentas creadas está en el rango de 1 a 5 el mensaje
    será: Campaña con poca afluencia

    b. Si el número de cuentas creadas está en el rango de 6 a 15 el mensaje
    será: Campaña moderada siga adelante

    c. Si el número de cuentas creadas está en el rango de 16 en adelante,
    el mensaje será: Excelente campaña

"""


def crearFacebook():
    usuario = str(input("Ingresa un nombre de usuario: "))
    edad = int(input("Ingresa tu edad: "))
    ciudad = str(input("Ingresa la ciudad en la que resides: "))
    pais = str(input("Ingresa el país que se encuentra la ciudad: "))
    correo = str(input("Ingresa tu correo electrónco: "))
    cadena = "El cliente crea una cuenta en Facebook con nombre de usuario %s\
              con un edad de %d años en %s - %s con un correo electrónico %s\n"\
              % (usuario,edad,ciudad,pais,correo)
    return cadena
    
def crearTwitter():
    nombres = str(input("Ingrese sus nombre completos: "))
    apellidos = str(input("Ingrese sus apellidos completos: "))
    usuario = str(input("Ingresa un nombre de usuario: "))
    edad = int(input("Ingresa tu edad: "))
    ciudad = str(input("Ingresa la ciudad en la que resides: "))
    pais = str(input("Ingresa el país que se encuentra la ciudad: "))
    idioma = str(input("Ingresa el idioma que se habla en el país: "))
    correo = str(input("Ingresa tu correo electrónco: "))
    print("El cliente %s %s crea una cuenta en Twitter que ingresa como\
nombre de usuario %s con una edad de %d años en %s - %s con un idioma %s e\
ingresa como correo electrónico %s\n" % (nombres,apellidos,usuario,edad,
                                             ciudad,pais,idioma,correo))

def crearWhatsApp():
    usuario = str(input("Ingresa un nombre de usuario: "))
    celular = int(input("Ingrese su número de celular: "))
    edad = int(input("Ingresa tu edad: "))
    ciudad = str(input("Ingresa la ciudad en la que resides: "))
    pais = str(input("Ingresa el país que se encuentra la ciudad: "))
    cadena = "El cliente crea una cuenta en WhatsApp ingresa como nombre de\
     usuario %s con número de celular %d tiene %d años de edad en %s - %s\n"\
    % (usuario,celular,edad,ciudad,pais)
    return cadena

def crearTelegram():
    usuario = str(input("Ingresa un nombre de usuario: "))
    celular = int(input("Ingrese su número de celular: "))
    edad = int(input("Ingresa tu edad: "))
    ciudad = str(input("Ingresa la ciudad en la que resides: "))
    pais = str(input("Ingresa el país que se encuentra la ciudad: "))
    areaInteres = str(input("Ingresa una área de interés: "))
    print("El cliente crea una cuenta en Telegram ingresa como nombre de \
usuario %s con número de celular %d tiene %d años de edad en %s - %s \
y tiene interés en la área de %s\n" % (usuario,celular,edad,ciudad,pais,
                                           areaInteres))

def crearSignal():
    usuario = str(input("Ingresa un nombre de usuario: "))
    celular = int(input("Ingrese su número de celular: "))
    edad = int(input("Ingresa tu edad: "))
    ciudad = str(input("Ingresa la ciudad en la que resides: "))
    pais = str(input("Ingresa el país que se encuentra la ciudad: "))
    hobby = str(input("Ingresa tu hobby principal: "))
    cadena = "El cliente crea una cuenta en Signal ingresa como nombre de \
    usuario %s con un número de celular %d en %s - %s, su hobby principal es \
    %s\n" % (usuario,celular,ciudad,pais,hobby)
    return cadena

def crearInstagram():
    usuario = str(input("Ingresa un nombre de usuario: "))
    edad = int(input("Ingresa tu edad: "))
    ciudad = str(input("Ingresa la ciudad en la que resides: "))
    correo = str(input("Ingresa tu correo electrónco: "))
    print("El cliente crea una cuenta en Instagram ingresa como nombre usuario \
%s tiene %d años de edad en la ciudad de %s con un correo electrónico %s\n"
          % (usuario,edad,ciudad,correo))

def crearFlickr():
    usuario = str(input("Ingresa un nombre de usuario: "))
    correo = str(input("Ingresa tu correo electrónco: "))
    cadena = "El cliente crea una cuenta en Flickr ingresa como nombre de \
usuario %s con un correo electrónica %s\n" % (usuario,correo)
    return cadena

def obtenerMensaje(contador):
    cadenaFinal = ""
    mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga\
                       adelante", "Excelente campaña"]
    if((contador >= 1) & (contador <= 5)):
        cadenaFinal = mensajeFinal[0]
    elif((contador >= 6) & (contador <= 15)):
        cadenaFinal = mensajeFinal[1]
    elif(contador >= 16):
            cadenaFinal = mensajeFinal[2]
    else:
        if(contador == 0):
            cadenaFinal = "No hay cuentas ingresadas" 
        

    return cadenaFinal

# Aquí empieza el proceso cuando se ejecuta por consola
# el archivo
# python run.py
if __name__ == "__main__":
    print("Proceso inicial")
    reporte = ""
    contador = 0
    bandera = True

    while(bandera):
        print("Ingrese una opción: ")
        print("Ingrese 1 para la cuenta de Facebook \ Ingrese 2 para la cuenta\
de Twitter \ Ingrese 3 para la cuenta de WhatsApp \ Ingrese 4\
para la cuenta de Telegram \ Ingrese 5 para la cuenta de Signal\
Ingrese 6 para la cuenta de Instagram \ Ingrese 7 para la cuenta de Flickr")
        opcion = int(input("Introduzca aqui su opción: "))
        
        if opcion == 1:
            cuenta_Facebook = crearFacebook()
        elif opcion == 2:
            crearTwitter()
        elif opcion == 3:
            cuenta_WhatsApp = crearWhatsApp()
        elif opcion == 4:
            crearTelegram()
        elif opcion == 5:
            cuenta_Signal = crearSignal()
        elif opcion == 6:
            crearInstagram()
        else:
            if opcion == 7:
                cuenta_Flickr = crearFlickr()

            
        if ((opcion >= 1) & (opcion <= 7)):
            contador = contador + 1
        else:
            print("Error, intente colocar los número presentados\n")

        print("Ingresar 2 para dejar de ingresar más datos\n")
        salir = int(input("Introduzca aqui: "))
        if (salir == 2):
            bandera = False

        reporte = obtenerMensaje(contador)
        print(reporte)
        
        
                    
        
