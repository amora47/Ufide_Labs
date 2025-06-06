# Lista vacia
beatles = []
#metodo apend para agregar ciertos miembros de la banda
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Paso 2",beatles)
#Paso 3 bucle for  y append 
for name in ['Stu Sutcliffe', 'Pete best']:
    new_member = input(f"Por favor agregue a {name}: ")
    beatles.append(new_member)
print("Paso 3", beatles)
del beatles[4]
del beatles[3]
print("Paso 4:", beatles)
#Agregar a Ringo 
beatles.insert(0, 'Ringo Starr')
print("Paso5: ", beatles)