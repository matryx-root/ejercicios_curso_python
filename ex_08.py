# Pedimos al usuario que ingrese un texto y la palabra a buscar
texto = input("Ingrese un texto: ")
palabra = input("Ingrese la palabra a buscar: ")

# Verificamos si la palabra está en el texto
if palabra in texto:
    print("Se encuentra la cadena en el texto.")
else:
    print("No se encuentra la cadena en el texto.")
