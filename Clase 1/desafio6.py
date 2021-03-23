# Escribir un programa que ingrese desde teclado una cadena de caracteres e imprima cuántas letras “a” contiene

cadena = input('cadena: ')

letras_a = 0

for car in cadena:
    if car == 'a':
        letras_a += 1

print(f'letras a: {letras_a}')