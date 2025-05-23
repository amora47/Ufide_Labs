income = float(input("Please enter your income: "))

# Lógica de cálculo del impuesto
if income <= 85528:
    tax = 0.18 * income - 556.02
else:
    tax = 14839.02 +(income - 85528)*0.32

# El país feliz nunca devuelve dinero
if tax < 0:
    tax = 0.0

# Mostrar el resultado redondeado a pesos totales
print(f"El impuesto es: {round(tax, 1)} pesos")



