# Pedimos al usuario que ingrese el peso y la altura de la persona
peso = float(input("Ingrese el peso de la persona en kilogramos: "))
altura = float(input("Ingrese la altura de la persona en metros: "))

# Calculamos el índice de masa corporal (IMC)
imc = peso / altura**2

# Imprimimos el resultado
print("El índice de masa corporal (IMC) es de:", imc)
