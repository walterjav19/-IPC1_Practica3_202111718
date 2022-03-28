from operator import index
from pickle import TRUE
from random import randint
opcion=0
premios=0
paredes=0
fantasmas=0
punteo=0
fila=randint(0,4)
columna=randint(0,5)
vida=1
nombre=""
ganar=False
tablero=[[" "," "," "," "," "," "]
        ,[" "," "," "," "," "," "]
        ,[" "," "," "," "," "," "]
        ,[" "," "," "," "," "," "]
        ,[" "," "," "," "," "," "]]

def imprimirtablero(pre,par,fan):
    for x in range(0,pre):
        fil=randint(0,4)
        col=randint(0,5)
        tablero[fil][col]="O"
    for x in range(0,par):
        fil=randint(0,4)
        col=randint(0,5)
        tablero[fil][col]="X"
    for x in range(0,fan):
        fil=randint(0,4)
        col=randint(0,5)
        tablero[fil][col]="@"
    tablero[fila][columna]="<"  

    print(f"--------------\nUsuario: {nombre}\nPunteo: {punteo}\nVidas: {vida}\n")
    print("---------------")
    for i in range(0,5):
         print("|",tablero[i][0],tablero[i][1],tablero[i][2],tablero[i][3],tablero[i][4],tablero[i][5],"|")
    print("---------------")


def actualizartablero():
    movimiento=input("")
    global fila
    global columna
    global punteo
    global ganar
    global vida
    if movimiento=="w":
        if tablero[fila-1][columna]=="O":
            punteo=punteo+10
        elif tablero[fila-1][columna]=="@":
            vida=vida-1
        elif tablero[fila-1][columna]=="X":
            fila=fila+1
        tablero[fila][columna]=" "
        fila=fila-1
        tablero[fila][columna]="<"        
        print("te moviste arriba")
        if tablero[fila][columna]=="O":
            punteo=punteo+10  
        print(f"--------------\nUsuario: {nombre}\nPunteo: {punteo}\nVidas: {vida}\n")
        print("---------------")
        for i in range(0,5):
            print("|",tablero[i][0],tablero[i][1],tablero[i][2],tablero[i][3],tablero[i][4],tablero[i][5],"|")  
        print("---------------")
    elif movimiento=="a":
        if tablero[fila][columna-1]=="O":
            punteo=punteo+10
        elif tablero[fila][columna-1]=="@":
            vida=vida-1
        elif tablero[fila][columna-1]=="X":
            columna=columna+1        
        tablero[fila][columna]=" "
        columna=columna-1
        tablero[fila][columna]="<"
        print("te moviste a la izquierda")
        print(f"--------------\nUsuario: {nombre}\nPunteo: {punteo}\nVidas: {vida}\n ")
        print("---------------")
        for i in range(0,5):
            print("|",tablero[i][0],tablero[i][1],tablero[i][2],tablero[i][3],tablero[i][4],tablero[i][5],"|")  
        print("---------------")
    elif movimiento=="s":
        if tablero[fila+1][columna]=="O":
            punteo=punteo+10
        elif tablero[fila+1][columna]=="@":
            vida=vida-1
        elif tablero[fila+1][columna]=="X":
            fila=fila-1            
        tablero[fila][columna]=" "
        fila=fila+1
        tablero[fila][columna]="<"
        print("te moviste abajo")
        print(f"--------------\nUsuario: {nombre}\nPunteo: {punteo}\nVidas: {vida}\n ")
        print("---------------")
        for i in range(0,5):
            print("|",tablero[i][0],tablero[i][1],tablero[i][2],tablero[i][3],tablero[i][4],tablero[i][5],"|")  
        print("---------------")
    elif movimiento=="d":
        if tablero[fila][columna+1]=="O":
            punteo=punteo+10
        elif tablero[fila][columna+1]=="@":
            vida=vida-1
        elif tablero[fila][columna+1]=="X":
            columna=columna-1           
        tablero[fila][columna]=" "
        columna=columna+1
        tablero[fila][columna]="<"
        print("te moviste a la derecha")
        print(f"--------------\nUsuario: {nombre}\nPunteo: {punteo}\nVidas: {vida}\n")
        print("---------------")
        for i in range(0,5):
            print("|",tablero[i][0],tablero[i][1],tablero[i][2],tablero[i][3],tablero[i][4],tablero[i][5],"|")  
        print("---------------")
    elif movimiento == "f":
        print("partida terminada")
        ganar=True
    if vida==0:
        ganar=True
        print("perdiste intenta de nuevo")

          



while opcion!=2:
    print("===== MENU DE INICIO =====\n1. Iniciar juego\n2. Salir")
    opcion= int(input())
    if opcion==1:
        nombre=input("Nombre de usuario: ")
        premios=randint(3,6)
        paredes=randint(5,12)
        fantasmas=randint(1,6)
        imprimirtablero(premios,paredes,fantasmas)
        while ganar !=True:
            actualizartablero()        
    elif opcion==2:
        print("Salio del juego")
    else:
        print("elija opcion 1 entra al juego u opcion 2 salir del juego")    
