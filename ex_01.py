# Pedimos al usuario que ingrese las dos notas
nota_teoria = float(input("Ingrese la nota de teoría: "))
nota_practica = float(input("Ingrese la nota de práctica: "))

# Calculamos el promedio
promedio = (nota_teoria + nota_practica) / 2

# Verificamos si el estudiante aprobó o no la materia
if promedio >= 4.0:
    print("Has aprobado la materia con un promedio de", promedio)
else:
    print("Has reprobado la materia con un promedio de", promedio)
