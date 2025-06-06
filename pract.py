# numero = [1,2,3,4,5]
# for num in numero:
#     print(numero)

# tablero = [
#     ['A','E','I'],
#     ['B','C','D']
# ]
# for list1 in tablero:
#     for letra in list1:
#         print(letra)
# tablero = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for fila in tablero:
#     print("Nueva fila:", fila)
#     for numero in fila:
#         print("Número en la fila:", numero)
# cursos = [
#     ["Ana", "Luis", "Marta"],
#     ["Pedro", "Sofía", "Carlos"],
#     ["Lucía", "Tomás", "Elena"]
# ]

# curso_num = 1  # Empezamos desde Curso 1

# for curso in cursos:  # Cada curso es una lista
#     print(f"Curso {curso_num}:")
#     for estudiante in curso:  # Cada estudiante en ese curso
#         print(f"- {estudiante}")
# #     print()  # Línea en blanco para separar cursos
# #     curso_num += 1
# numeros = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]
# contador = 1
# for num_fila in numeros: 
#     print(f"Fila {contador}:", end=" ")
#     for num_total in num_fila:
#         print(num_total, end=", ")
#     print()  
#     contador +=1         

valores = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
contador = 0
for val in valores:
    for num in val:
        contador += num
print(contador)