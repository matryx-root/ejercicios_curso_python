# Pedimos al usuario que ingrese la altura y la base del rectángulo
altura = int(input("Ingrese la altura del rectángulo: "))
base = int(input("Ingrese la base del rectángulo: "))

# Dibujamos el rectángulo utilizando asteriscos
for i in range(altura):
    for j in range(base):
        print("*", end="")
    print()

# Imprimimos el mensaje de fin de programa
print("Fin de programa")
