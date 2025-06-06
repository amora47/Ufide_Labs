#Ejercicio 1 
fila = [1, 2, 3]
# print("[", end="")
for celda in fila:
         print(f"[ {celda} ]", end="")
print()

#Ejercicio 2
fila1 = [1,2,3]
fila2 = [4,5,6]
for celda in fila1:
        print(f"|{celda}|", end="")
print()
for cel in fila2:
        print(f"|{cel}|", end="")
print()
#Ejercicio3
tablero = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for fila3 in tablero:
        for i, celda in enumerate(fila3):
            if celda == 5: 
                   fila3[i] = "X"
for fila in tablero:
       print(fila)
        
#Ejercicio 4
palabras = ["hola", "mundo", "hola", "python"]
for i, caracter in enumerate(palabras):
       if caracter == "hola":
              palabras[i] = "Hello"
print(palabras)                      