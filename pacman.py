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
    global vida
    global punteo
    vida=1
    punteo=0
    print(f"--------------\nUsuario: {nombre}\nPunteo: {punteo}\nVidas: {vida}\n")
    print("---------------")
    for i in range(0,5):
         print("|",tablero[i][0],tablero[i][1],tablero[i][2],tablero[i][3],tablero[i][4],tablero[i][5],"|")
    print("---------------")


def actualizartablero():
    global ganar
    movimiento=input("")
    global fila
    global columna
    global punteo
    global vida
    if movimiento.lower()=="w":
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
        print(f"--------------\nUsuario: {nombre}\nPunteo: {punteo}\nVidas: {vida}\n")
        print("---------------")
        for i in range(0,5):
            print("|",tablero[i][0],tablero[i][1],tablero[i][2],tablero[i][3],tablero[i][4],tablero[i][5],"|")  
        print("---------------")
    elif movimiento.lower()=="a":
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
    elif movimiento.lower()=="s":
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
    elif movimiento.lower()=="d":
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
    elif movimiento.lower() == "f":
        print("partida terminada")
        ganar=True
    if vida==0:
        ganar=True
        print("perdiste intenta de nuevo")
    if tablero[0][0]!="O" and tablero[0][1]!="O" and tablero[0][2]!="O" and tablero[0][3]!="O" and tablero[0][4]!="O" and tablero[0][5]!="O" and tablero[1][0]!="O" and tablero[1][1]!="O" and tablero[1][2]!="O" and tablero[1][3]!="O" and tablero[1][4]!="O" and tablero[1][5]!="O" and tablero[2][0]!="O" and tablero[2][1]!="O" and tablero[2][2]!="O" and tablero[2][3]!="O" and tablero[2][4]!="O" and tablero[2][5]!="O" and tablero[3][0]!="O" and tablero[3][1]!="O" and tablero[3][2]!="O" and tablero[3][3]!="O" and tablero[3][4]!="O" and tablero[3][5]!="O" and tablero[4][0]!="O" and tablero[4][1]!="O" and tablero[4][2]!="O" and tablero[4][3]!="O" and tablero[4][4]!="O" and tablero[4][5]!="O":
        ganar=True        
        print("Ganaste Felicidades!!!!!")
            
while opcion!=2:
    print("===== MENU DE INICIO =====\n1. Iniciar juego\n2. Salir")
    opcion= int(input())
    if opcion==1:
        nombre=input("Nombre de usuario: ")
        premios=randint(3,6)
        paredes=randint(5,12)
        fantasmas=randint(1,6)
        imprimirtablero(premios,paredes,fantasmas)
        ganar=False
        while ganar !=True:
            actualizartablero()        
    elif opcion==2:
        print("Salio del juego")
    else:
        print("elija opcion 1 entra al juego u opcion 2 salir del juego")    
