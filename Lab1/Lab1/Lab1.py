def menu():
    print(" ")
    print("***Operaciones***")
    print (" ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Numero Primo")
    print("6. Numero Palindromo")
    print("7. Salir")
    opcion = input ("Escriba la opcion:")
    opcion = int(opcion)
    if opcion==1: suma()
    elif opcion==2: resta()
    elif opcion==3: multiplicacion()
    elif opcion==4: division()
    elif opcion==5: primo()
    elif opcion==6: palindromo()
    else: exit()  

def suma():
    print("")
    print ("***Suma***")
    numero1 = input("Numero 1: ")
    numero2 = input("Numero 2: ")
    numero1 = float(numero1)
    numero2 = float(numero2)
    print ("Resultado: ", numero1+numero2)
    print("")
    menu()
    
def resta():
    print("")
    print ("***Resta***")
    numero1 = input("Numero 1: ")
    numero2 = input("Numero 2: ")
    numero1 = float(numero1)
    numero2 = float(numero2)
    print ("Resultado: ", numero1-numero2)
    print("")
    menu()

def multiplicacion():
    print("")
    print ("***Multiplicacion***")
    numero1 = input("Numero 1: ")
    numero2 = input("Numero 2: ")
    numero1 = float(numero1)
    numero2 = float(numero2)
    print ("Resultado: ", numero1*numero2)
    print("")
    menu()

def division():
    print("")
    print ("***Division***")
    numero1 = input("Numero 1: ")
    numero2 = input("Numero 2: ")
    numero1 = float(numero1)
    numero2 = float(numero2)
    print ("Resultado: ", numero1/numero2)
    print("")
    menu()

def primo(numero):
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        for temporal in range(2, numero):
            if numero % temporal == 0:
                return False
        return True            

def app():
    numero = int(input("Escribe un numero: "))
    result = primo(numero)

    if result is True:
        print("El numero es primo")
    else:
        print("El numero no es primo")

if __name__ == '__main__':
    app()
def palindromo():
    igual, auxiliar = 0, 0
    texto = input("Ingrese la palabra o numero a evaluar: ")
    for indice in reversed(range(0, len(texto))):
        if texto[indice].lower() == texto[auxiliar].lower():
            igual += 1
            auxiliar += 1
        if len(texto) == igual:
            print("Es palindromo")
        else:
            print("No es palindromo")
    menu()

menu()