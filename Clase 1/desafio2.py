# ingresar un número desde el teclado e imprimir si es múltiplo de 2, 3 o 5

num = int(input('número: '))


if num % 2 == 0:
    print('multiplo de 2')
elif num % 3 == 0:
    print('multiplo de 3')
elif num % 5 == 0:
    print('multiplo de 5')