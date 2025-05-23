year = int(input('Enter the year that you want to calculate: '))

if year < 1582:
    print('No dentro del período del calendario Gregoriano')
else:
    if year % 4 != 0:
        print('Año Común')
    elif year % 100 != 0:
        print('Año Bisiesto')
    elif year % 400 != 0:
        print('Año Común')
    else:
        print('Año Bisiesto')