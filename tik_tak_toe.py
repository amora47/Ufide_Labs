#Importa librerias 
from random import randrange
#Se Inicializa la lista tablero vacia
tablero = []
#Se agrega un contador
contador = 1
#Se hace la lista dentro de otra lista 
for fila in range(3):
    fila_actual = []
    for columna in range(3):
        fila_actual.append(contador)
        contador += 1
    tablero.append(fila_actual)
# Funcion para mostrar el tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print("+-----+-----+")
        print("|", end="")
        for celda in fila:
             print(f" {celda} |",end="")
        print()
    print("+-----+-----+")
mostrar_tablero(tablero)
print("Movimiento #1 la maquina empieza:")
#Movimiento 1 el cual empieza el bot 
#Se utiliza el metodo enumerate para recorrer la fila en el tablero y obtener su indice
for i, fila in enumerate(tablero):
    #Se utilia el metododo enum para recorrer y obtener el indice de la celda en la fila
    for j, celda in enumerate(fila):
        if celda == 5:
            tablero[i][j] = "X"
mostrar_tablero(tablero)

# Funcion para marcar movimiento en el tablero
def marcar_tablero(tablero,numero,simbolo):
    for i, fila in enumerate(tablero):
        for j,celda in enumerate(fila):
            if celda == numero:
                tablero[i][j] = simbolo
                return True
    return False
# Movimiento 2 Humano 
def movimiento_humano(tablero):
    while True:
        mov_humano = int(input("Por favor seleccione un numero del 1 al 9:"))
        if marcar_tablero(tablero, mov_humano, "o"):
            print("Movimiento valido")
            mostrar_tablero(tablero)
            break
        else:
            print("Movimiento Invalido")
            mostrar_tablero(tablero)

    
def movimiento_bot(tablero):
    opciones_libres = []
    for fila in tablero:
        for celda in fila:
            if isinstance(celda,int):
                opciones_libres.append(celda)
    if opciones_libres:
        movimiento = opciones_libres[randrange(len(opciones_libres))]
        marcar_tablero(tablero,movimiento, "X")

def juego_terminado(tablero):
    for fila in tablero:
        for columna in fila:
            if isinstance(columna,int):
                return False
    return True
def ganador(tablero, simbolo):
    for fila in tablero:
       if all(celda == simbolo for celda in fila):
           return True
    for col in range(3):
        if all(tablero[fila][col] == simbolo for fila in range(3)):
            return True
    if all(tablero[i][i] == simbolo for i in range(3)):
        return True
    if all(tablero[i][2 - i] == simbolo for i in range(3)):
        return True

    return False   


while True:
    movimiento_humano(tablero)
    if ganador(tablero, "o"):
        print("¡Ganaste tú!")
        break
    if juego_terminado(tablero):
        print("¡Empate!")
        break

    movimiento_bot(tablero)
    mostrar_tablero(tablero)
    if ganador(tablero, "X"):
        print("¡Gana la máquina!")
        break
    if juego_terminado(tablero):
        print("¡Empate!")
        break

