def futuro(edad):
    edad = edad + 1


def pasado():
    global edad
    edad = edad - 1


edad = int(input('Ingresa tu edad: '))
resp = int(input("""Elige una opción:
                    1.- El año que viene tu edad será...
                    2.- El año pasado tu edad era.... 
                """))

if resp == 1:
    futuro(edad)
else:
    pasado()

print(edad)
