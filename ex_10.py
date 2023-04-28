rut = input("Ingresa tu RUT sin puntos ni dígito verificador: ")
numero = rut[::-1] # invertimos el RUT para poder multiplicar por la serie
serie = [2, 3, 4, 5, 6, 7]
suma = 0
for i in range(len(numero)):
    suma += int(numero[i]) * serie[i % 6] # multiplicamos por la serie
resto = suma % 11
dv = 11 - resto if resto != 0 else "0" # aplicamos las reglas
dv = "K" if dv == 10 else str(dv)
print(f"Su dígito verificador es {dv}")
