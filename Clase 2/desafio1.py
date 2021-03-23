# Modificar el código previa para que se imprima la cadena “TIENE R” si la palabra contiene la letra r y sino, imprima “NO TIENE R”.

for i in range(4):
    cadena = input('cadena: ')
    if 'r' in cadena:
        print('TIENE R')
    else:
        print('NO TIENE R')
