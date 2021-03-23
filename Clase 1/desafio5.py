# Dadas dos cadenas ingresadas desde el teclado, imprimir aquella que tenga más caracteres.

cadena1 = input('primer cadena: ')
cadena2 = input('segunda cadena: ')

if len(cadena1) > len(cadena2):
    print(cadena1)
else:
    print(cadena2)