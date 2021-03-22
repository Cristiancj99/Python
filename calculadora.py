fin = False

print('CALCULADORA')
print('Seleccione la opcion: ')
print('opcion 1: suma')
print('opcion 2: resta')
print('opcion 3: multiplicacion')
print('opcion 4: division')
print('opcion 5: salir')

#bucle que utilizaremos para esta pidiendo continuamente datos. se repetirá siempre que fin NO sea true
while not (fin):
    opcion =int( input('Seleccione la opcion deseada: '))

    if(opcion == 1):
        #Debemos indicar que tipo de variable es lo obtenido por pantalla.
        sumando1 = int (input("Introduzca el primer numero"))
        sumando2 = int (input("Introduzca el segundo numero"))
        print('El resultado de la suma es de: ', sumando1 + sumando2)
    elif(opcion == 2):
        resto1 = int (input("Introduzca el primer numero"))
        resto2 = int (input("Introduzca el segundo numero"))
        print('El resultado de la resta es de: ', resto1 - resto2)
    elif(opcion == 3):
        multiplicando = float( input("Introduzca el multiplicando"))
        multiplicador = float (input("Introduzca el multiplicador"))
        print('El resultado de la resta es de: ', multiplicando * multiplicador)
    elif(opcion == 4):
        dividendo = float(input("Introduzca el dividendo"))
        divisor = float (input("Introduzca el divisor"))
        print('El resultado de la division es de: ', dividendo  / divisor)
    elif(opcion == 5):
        fin=True
