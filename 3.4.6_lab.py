hat = [1, 2, 3, 4, 5]

# Paso 1: Reemplazar el número central (índice 2)
hat[2] = int(input("Ingresa un número entero para reemplazar el número central: "))

# Paso 2: Eliminar el último elemento
hat.pop()

# Paso 3: Imprimir la longitud de la lista
print(len(hat))