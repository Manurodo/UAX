from Class import BankAccount
from random import randint

print(" ")
print ("Por favor introduzca su MyBank ID")
print(" ")
print ("Si no tiene un MyBank ID introduzca su nombre y le proporcionaremos un MyBank ID nuevo")
print(" ")

in_ = input ("|: ") #Introduce ID necesaria para la implementacion de la clase

try:
    int(in_) #Si no introduces un numero se considera que elegiste no escribir el ID y se genera uno nuevo
    ID = in_
except:
    ValueError
    name = in_
    ID = randint (10000, 99999) #El id generado es un num aleatorio del 10000 al 99999
    print(" ")
    print ("Buenas tardes",name,"soy su asistente personal del Banco MyManueBank y su nuevo ID es :", ID)
    print(" ")
else:
    print(" ")
    print ("Buenas tardes Client ID nº",in_,"soy su asistente personal del Banco MyManueBank")

Costumer = BankAccount (ID)
while True:
    print(" ")
    print ("De entre los siguientes comandos introduzca la accion que le gustaría realizar:")
    print (" ")
    print ("1.Depositar: introduce la cantidad deseada dentro de su cuenta")
    print ("2.Retirar: retire la cantidad indicada de su cuenta")
    print ("3.Comprobar: Compruebe el balance de su cuenta")
    print ("4.Salir: Si quiere salir del programa")
    print(" ")
    comm = input ("|: ")

    while comm not in ["1", "2", "3", "4" , "Depositar", "Retirar", "Comprobar", "Salir"]: 
        print(" ")
        print("Comando inválido, por favor introduzca un número o nombre de comando válido.")
        print(" ")
        comm = input("|:")
    #Bucle declarando que mientras no se inpute un valor de comando valido no se procedera a continuar 
    if comm == "Depositar" or comm == "1":
        print(" ")
        print ("Introduzca cantidad a depositar")
        print(" ")
        quant = float (input ("|:"))
        print (Costumer.depositar(quant))
    #1er comando "Depositar", añade un valor numerico al balance del ID 
    if comm == "Retirar" or comm == "2":
        print(" ")
        print ("Introduzca cantidad a retirar")
        print(" ")
        quant = float (input ("|:"))
        print (Costumer.retirar(quant)) 
    #2do comando "Retirar", añade un valor numerico al balance del ID
    if comm == "Comprobar" or comm == "3":
        print(Costumer.cantidad())
    #3er comando ""
    if comm == "Salir" or comm == "4":
        print(" ")
        print ("Que tenga un buen día y gracias por utilizar MyManueBank")
        print(" ")
        break