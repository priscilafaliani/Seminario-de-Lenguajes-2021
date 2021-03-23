# Ingresar palabras desde el teclado hasta ingresar la palabra FIN. Imprimir aquellas que empiecen y terminen con la misma letra.

cadena = input('palabra: ')

while cadena != 'FIN':
    if len(cadena) > 0 and cadena.endswith(cadena[0]):
        print(cadena)
    cadena = input('palabra: ')