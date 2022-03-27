from random import randint
opcion=0
premios=0
paredes=0
fantasmas=0
punteo=0
posicionx=0
posiciony=0
nombre=""
tablero=[[" "," "," "," "," "," "]
        ,[" "," "," "," "," "," "]
        ,[" "," "," "," "," "," "]
        ,[" "," "," "," "," "," "]
        ,[" "," "," "," "," "," "]]

def imprimirtablero(pre,par,fan):
    for x in range(0,pre):
        posicionx=randint(0,4)
        posiciony=randint(0,5)
        tablero[posicionx][posiciony]="O"
    for x in range(0,par):
        posicionx=randint(0,4)
        posiciony=randint(0,5)
        tablero[posicionx][posiciony]="X"
    for x in range(0,fan):
        posicionx=randint(0,4)
        posiciony=randint(0,5)
        tablero[posicionx][posiciony]="@"


    print(f"--------------\nUsuario: {nombre}\nPunteo: {punteo} ")
    print("---------------")
    for i in range(0,5):
         print("|",tablero[i][0],tablero[i][1],tablero[i][2],tablero[i][3],tablero[i][4],tablero[i][5],"|")
    print("---------------")

def imprimirpos(fila,columna):
    print(fila,columna)


while opcion!=2:
    print("===== MENU DE INICIO =====\n1. Iniciar juego\n2. Salir")
    opcion= int(input())
    if opcion==1:
        nombre=input("Nombre de usuario: ")
        premios=randint(3,6)
        paredes=randint(5,12)
        fantasmas=randint(1,6)
        imprimirtablero(premios,paredes,fantasmas)
        print(premios,paredes,fantasmas)
        imprimirpos(posicionx,posiciony)
        move=input("")                     
    elif opcion==2:
        print("Salio del juego")
    else:
        print("elija opcion 1 entra al juego u opcion 2 salir del juego")    
