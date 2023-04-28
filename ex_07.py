# Pedimos al usuario que ingrese un número entero entre 1 y 19
numero = int(input("Ingrese un número entero entre 1 y 19: ==> "))

# Validamos que el número ingresado esté dentro del rango permitido
if numero < 1 or numero > 19:
    print("El número ingresado no está dentro del rango permitido.")
else:
    # Imprimimos los números del 1 al 19, saltando el número ingresado
    for i in range(1, 20):
        if i != numero:
            print(i, end="-- ")
    print("\nTerminé")
