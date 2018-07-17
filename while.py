
numero_ingresado = 10


while numero_ingresado > 0 :

    print(numero_ingresado)

    numero_ingresado -= 1

    nuevo = input("Desea ingresar nuevos valores?")

    if nuevo == "SI":

        valor = int (input("ingrese nuevo numero"))


    else:
        print("ya nada")
