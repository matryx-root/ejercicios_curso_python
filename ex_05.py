
# Pedimos al usuario que ingrese dos números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

# Encontramos el número más pequeño y el número más grande
min_num = min(num1, num2)
max_num = max(num1, num2)

# Inicializamos contadores para los números pares y la suma de los pares
num_pares = 0
sum_pares = 0

# Imprimimos los números entre los dos números ingresados, y contamos los pares y su suma
for i in range(min_num, max_num + 1):
    print(i)
    if i % 2 == 0:
        num_pares += 1
        sum_pares += i

# Imprimimos el resultado
print(f"Entre {min_num} y {max_num} hay {max_num - min_num +1} números siendo {num_pares} pares")
print(f"La suma de los pares es {sum_pares}")
