tablero = [
    '-*-*-',
    '--*--',
    '----*',
    '*----'
]


# retorna un nuevo string con la casilla incrementada
def renovar_string(a_modificar, pos, value):
    """Recibe un string y sólo modifica el caracter en pos remplazandolo por value

        Parametros:
            a_modificar : str -> el string que se va a modificar
            pos : int -> la posición del caracter que se debe actualizar
            value : str -> el valor que se debe colocar en pos
    """
    output = ''
    for i in range(len(a_modificar)):
        if i == pos:
            output += value
        else:
            output += a_modificar[i]
    return output


def incrementar_casilla(tablero, linea_casilla, pos_x_casilla):
    """Incrementa en 1 una casilla dada del tablero.

        Para incrementar es necesario utilizar el método renovar_string, dado que los strings no son mutables.
        El método se encarga de pasar los valores necesarios para crear el nuevo string al método mencionado.

        Parámetros:
            tablero : list,
            linea_casilla : int,
            pos_x_casilla : int

        Ejemplo:
            tablero -> ['00000', '0*000', '00000']

            linea_casilla = 1
            pos_x_casilla = 0

            resultado -> ['00000', '1*000', '00000']
    """
    valor_casilla_incrementada = str(int(tablero[linea_casilla][pos_x_casilla]) + 1)
    tablero[linea_casilla] = renovar_string(tablero[linea_casilla], pos_x_casilla, valor_casilla_incrementada)


def incrementar_linea(tablero, linea_mina, centro):
    """Recibe la posición de una línea en el tablero + un pivot a partir del cual actualiza las casillas a izq/der/el mismo pivot, si no son minas.

        El mismo verifica que existan casillas a izquierda/derecha y que ninguna sea una mina (incluyendo el pivot).
        Luego de las verificaciones, incrementa en 1 la cantidad de minas en cada casilla.

        Parámetros:
            tablero : list 

            linea_mina : int -> la línea del tablero que se va a modificar

            centro : int -> el pivot al partir del cuál se actualizan las casillas alrededor

        Ejemplo:
            tablero -> ['00000', '0*000', '00000']

            linea_mina = 1
            centro = 1

            resultado -> ['00000', '1*100', '00000']
    """
    # si hay casilla a la izquierda
    if centro - 1 >= 0:
        # si no es una mina
        if not tablero[linea_mina][centro - 1] == '*':
            # incremento
            incrementar_casilla(tablero, linea_mina, centro - 1)
            
    # si hay casilla a la derecha
    if centro + 1 < len(tablero[linea_mina]):
        # si no es una mina
        if not tablero[linea_mina][centro + 1] == '*':
            # incremento
            incrementar_casilla(tablero, linea_mina, centro + 1)

    # si el 'centro' no es la casilla de la mina misma
    if not tablero[linea_mina][centro] == '*':
        incrementar_casilla(tablero, linea_mina, centro)


# recibe la posicion de una mina e incrementa en 1 todas las casillas alrededor (que no sean minas)
def incrementar_minas(tablero, linea_mina, pos):
    """Recibe la posición de una mina en el tablero y actualiza la cantidad de minas en las casillas de alrededor

        El método recibe la posición de la mina en el tablero y debe actualizar:
            * Las casillas de la izquierda/derecha (queda en manos del método incrementar_linea)
            * Las líneas de arriba/abajo.
        El método verifica los límites de arriba/abajo.
        El método NO verifica los límites a izquierda/derecha. Eso queda en manos del método incrementar_linea

        Parámetros:
            tablero : list 
            
            linea_mina : int -> linea donde está la mina
            pos : int -> casilla de la línea dónde está la mina

        Ejemplos:
            tablero -> ['-----', '-*---', '-----']

            linea_mina = 1
            pos = 1

            resultado -> ['111--', '1*1--', '111--']            
    """

    # si hay linea arriba
    if linea_mina - 1 >= 0:
        incrementar_linea(tablero, linea_mina - 1, pos)

    # si hay linea abajo
    if linea_mina + 1 < len(tablero):
        incrementar_linea(tablero, linea_mina + 1, pos)

    # también incrementar en la linea actual
    incrementar_linea(tablero, linea_mina, pos)


def preparar_tablero(tablero):
    """Modifica el tablero de forma tal que los '-' sean remplazados por '0'

        Esta función facilita la utilización del método 'incrementar_casilla'
        y a su vez, que las casillas que no tengan minas alrededor no queden en '-'
        luego del llamado a 'contar_minas'

        Parámetros:
            tablero : list -> ['-----', '-*---', ....]

        Output:
            tablero -> ['00000', '0*000', ....]
    """
    # recorre cada línea
    for i in range(len(tablero)):
        # el string de la línea es actualizado
        tablero[i] = tablero[i].replace('-', '0')


def contar_minas(tablero):
    """Modifica el tablero de forma tal que cada casilla muestre el número de minas alrededor

        Parámetros:
            tablero : list -> ['-----', '-*---', ....]
    """
    preparar_tablero(tablero)

    # recorre cada linea
    for i in range(len(tablero)):
        # recorre cada caracter
        for j in range(len(tablero[i])):
            # si es una mina
            if tablero[i][j] == '*':
                incrementar_minas(tablero, i, j)


def imprimir_tablero(tablero):
    """Imprime el tablero en forma de matriz
    
        Parámetros:
            tablero : list
    """
    # recorre cada línea
    for i in range(len(tablero)):
        # imprime cada caracter, separados por espacio
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=' ')
        print()


print('ANTES')
print()
imprimir_tablero(tablero)
print()
contar_minas(tablero)
print('DESPUÉS')
print()
imprimir_tablero(tablero)
print()


