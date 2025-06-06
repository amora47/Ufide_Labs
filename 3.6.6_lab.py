my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unique_list = []
for number in my_list:
    if number not in unique_list:
        unique_list.append(number)

print("Lista original:", my_list)
print("Lista sin duplicados:", unique_list)