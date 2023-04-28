# Pedimos al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Imprimimos la tabla de multiplicar del número ingresado
print("Tabla de multiplicar de", numero)
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
