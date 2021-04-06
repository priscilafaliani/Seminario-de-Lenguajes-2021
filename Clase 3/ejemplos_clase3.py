def imprimo1(uno, dos, tres, cuatro):
    print(f'{uno}, {dos}')


def imprimo2(*args):
    for valor in args:
        print(valor)


def imprimo3(**kwargs):
    for nombre, valor in kwargs.items():
        print(f'{nombre} = {valor}')


tabla_numeros = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4}

imprimo3(**tabla_numeros)
print('-' * 20)

imprimo3(uno=1, dos=2, tres=3, cuatro=4)
print('-' * 20)

imprimo1(uno='I', dos='II', tres='III', cuatro='IV')
print('-' * 20)

imprimo1('I', 'II', 'III', 'IV')
print('-' * 20)

imprimo2(1, 2, 3, 4)