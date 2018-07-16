
apetece_helado_s = input("Te apetece un helado?  (SI/NO): ").upper()

if apetece_helado_s == "SI":
    apetece_helado_s = True
elif apetece_helado_s == "NO":
    apetece_helado_s = False
else:
    print("dato incorrecto ingresado")
    apetece_helado_s = False


Tienes_Dinero_s = input("Tienes Dinero para un Helado (SI/NO)").upper()
Senor_de_helados_s = input("Se encuentra el Señor de los Helados? (SI/NO)").upper()
Esta_Tia_s = input("Estas con tu tia? (SI/NO)").upper()

apetece_helado = apetece_helado_s == "SI"
tiene_dinero = Tienes_Dinero_s == "SI" or Esta_Tia_s
senor_helados = Senor_de_helados_s == "SI"
print (apetece_helado)


if apetece_helado and tiene_dinero and senor_helados:
    print  ("Pues comete un helado")

else:
    print("Pues andate a la mierda")