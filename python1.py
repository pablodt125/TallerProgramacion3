from os import system

def grados(n):
    n=(n*(9/5))+32
    return n
def piramide(n):
    for i in range(1,n+1):
        for m in range((2*i)-1,0,-2):
            print(m,end=" ")
        print()

def horas(h,m,s):
    if h>=0 and h<24 and m<60 and m>=0 and s<60 and s>=0:
        print("La hora es valida.")
    else:
        print("La hora no es valida.")
def digitos(n):
    cont=0
    a=[]
    while n//10!=0:
        cont+=1
        a.append(n%10)
        n=n//10
    a.append(n)
    for i in range(cont,-1,-1):
        print(a[i],end=" ")
    print("\nEl numero de digitos es: ",cont+1)

def numeroPerfecto(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i;
    if n==sum:
        print("\n\nEl numero es perfecto.")
    else:
        print("\n\nEl numero no es perfecto")
    
def factorial(n):
    fac=1;
    for n in range(0,n+1):
        if n==0:
            print(fac,end=" ")
        else:
            for i in range(1,n+1):
                fac*=i
            print(fac,end=" ")
        fac=1

def cifradoCesar(cadena):
    abecedario=("abcdefghijklmnopqrstuwvxyz")
    cadena=cadena.lower()
    a=[]
    for i in range(0,len(cadena)):
        for n in range(0,len(abecedario)):
            if cadena[i]==abecedario[n]:
                a.append(abecedario[(n+3)%26])
    
    cad="".join(a)
    print(cad)
def frutas(n,m):
    diccionario={"platano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.7}
    l=False
    for i in diccionario:
        if i==n:
            print("El valor de la fruta son ",m*diccionario[i]," dolares")
            l=True
    if l==False:
        print("La fruta no esta disponible")


def menu():
    print("Introduzca un numero para seleccionar una de las siguientes opciones: \n1. Convertir de centigrados a Farenheint: ")
    print("2. Imprimir un triangulo de numeros enteros. ")
    print("3. Comprobar la hora. ")
    print("4. Imprimir digitos y saber la cantidad de digitos.")
    print("5. Verificar si un numero es perfecto. ")
    print ("6. Imprimir el factorial hasta un numero n. ")
    print("7. Cifrado Cesar.")
    print("8. Saber el precio de las frutas disponibles segun la cantidad de kilos.")
    print("0. Si deseas salir del programa.")


num=True
while num:
    menu()
    num=int(input(">>"))
    if num==1:
        system("cls")
        n=int(input("Intoduzca los centigrados que quieres convertir: "))
        print(grados(n))
        num=True
        n=(input())
        system("cls")
    elif num==2:
        system("cls")
        n=int(input("Introduzca el numero de filas del triangulo: "))
        piramide(n)
        n=(input())
        system("cls")
        num=True
    elif num==3:
        system('cls')
        hora=input()
        lista=[int(x) for x in hora.split(":")]
        a=lista[0]
        b=lista[1]
        c=lista[2]
        horas(a,b,c)
        n=(input())
        num=True
        system ("cls")
    elif num==4:
        system("cls")
        n=int(input("Ingrese un numero: "))
        digitos(n)
        n=(input())
        num=True
        system("cls")
    elif num==5:
        system("cls")
        n=int(input("Introduzca un numero: "))
        numeroPerfecto(n)
        n=(input())
        num=True
        system("cls")
    elif num==6:
        system("cls")
        n=int(input("Introduzca un numero: "))
        factorial(n)
        n=(input())
        num=True
        system("cls")
    elif num==7:
        system("cls")
        n=input("Introduzca una palabra: ")
        print("La cadena cifrada es: ",end=" ")
        cifradoCesar(n)
        n=(input())
        num=True
        system("cls")
    elif num==8:
        system("cls")
        frut=input("Que fruta desea: ")
        kilos=int(input("Cuantos kilos desea: "))
        frutas(frut,kilos)
        n=(input())
        num=True
        system("cls")
    elif num>8 or num<0:
        system("cls")
        print ("La opcion no es valida.")
        n=input(">>")
        num=True
        system("cls")
    elif num==0:
        system("cls")
        print ("Gracias por utilizar el programa. Feliz dia :D")
        n=input()
        num=False
        system("cls")