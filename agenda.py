salida = False

Agenda = dict()


while not salida:

    accion = input("Que deseas hacer? ").upper()

    if accion == "A":
        print("se añadira numero")
        nombre = input("nombre:\n ")
        print ("-"*10)
        numero = input("numero:\n ")

        Agenda[nombre] = numero

    elif accion == "C":

        print("se consultara numero")
        print ("-"*10)

        nombre = input("nombre  a consultar ")

        for filtro in Agenda:
            if nombre == filtro:

                print("resultado: ",nombre,":", Agenda[nombre])

        else:
                print("sin resultado")

    elif accion == "S":
        salida = True


    elif accion == "X":

        print("-"*5,"DICCIONARIOS", "-"*5)

        dicc = {2:"dos", 3:"tres", 4:"cuatro", 1:"uno"}

        posicion = int(input("posicion? "))

        print(dicc[posicion])
        valor = input("ingrese valor de ")
        agregado = int(input("nuevo dato: "))

        dicc[agregado] = valor

    elif accion == "E":
        texto = input("ingrese texto: ")
        palabra = input("ingrese clave a contar: ")
        veces = 0

        lista_palabras = texto.split()
        lista = []

        for contador in lista_palabras:



            if contador == palabra:
                print("= ",contador)

                veces +=1

        print("numero de repeticiones: ",veces)




print("bre")
