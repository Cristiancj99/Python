#Definicion de funciones.
def sumar():
    sumando1 = int (input("Introduzca el primer numero"))
    sumando2 = int (input("Introduzca el segundo numero"))
    print('El resultado de la suma es de: ', sumando1 + sumando2)
def restar():
    resto1 = int (input("Introduzca el primer numero"))
    resto2 = int (input("Introduzca el segundo numero"))
    print('El resultado de la resta es de: ', resto1 - resto2)
def multiplicar(): 
    multiplicando = float( input("Introduzca el multiplicando"))
    multiplicador = float (input("Introduzca el multiplicador"))
    print('El resultado de la resta es de: ', multiplicando * multiplicador)

def dividir():
    dividendo = float(input("Introduzca el dividendo"))
    divisor = float (input("Introduzca el divisor"))
    print('El resultado de la division es de: ', dividendo  / divisor)
def salir ():
    return True
#MAIN
fin = False

print('CALCULADORA')
print('Seleccione la opcion: ')
print('opcion 1: suma')
print('opcion 2: resta')
print('opcion 3: multiplicacion')
print('opcion 4: division')
print('opcion 5: salir')

while not (fin):
    opcion =int( input('Seleccione la opcion deseada: '))

    if(opcion == 1):
        sumar()

    elif(opcion == 2):
        restar()
    elif(opcion == 3):
        multiplicar()
    elif(opcion == 4):
        dividir()
    elif(opcion == 5):
        fin=salir()
