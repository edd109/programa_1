from datetime import datetime


class Contacto :
    def  __init__(self, nombre, apellido, numero, email, fecha):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.email = email
        self.fecha = fecha

        registro = []




Usuario_registrados = int(input("Cuantos ususario desea ingresar? (Max 3)\n"))

while Usuario_registrados > 0 :

    nombre_s = input("Ingrese nombre de usuario:\n")
    apellido_s = input("Ingrese apellido del usuario:\n")
    numero_s = input("Ingrese numero del usuario:\n")
    email_s = input("Ingrese e-mail del usuario:\n")
    fecha_s = input("Ingrese fecha del usuario:\n")

    contacto = Contacto(nombre=nombre_s, apellido=apellido_s, numero= numero_s, email = email_s, fecha= fecha_s)
    usuario_2 = Contacto (nombre= "Andres", apellido= "Tarado", numero= "345", email = "asas@gmail.com", fecha= "08/05/96")





    solicitud = input("desea mostrar nombre de usuario? (SI/NO)\n")

    if solicitud == "SI":

        print ("El nombrbre del usuario es ", contacto.nombre)
        print("Los datos completos del usuario son ", contacto)


    else:
        print ("Bueno ya nada")


    Usuario_registrados -= 1

continuar_registro = input("desea agregar mas usuarios?(SI/NO)\n" )

if continuar_registro == "SI":

    Usuario_adicionales = int (input("Ingrese numero de usuarios nuevos (Max 2)\n"))
    print("Se agregaron ",Usuario_adicionales," al registro")

else:
    print("Bueno ya nada")

