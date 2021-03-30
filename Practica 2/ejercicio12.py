tablero = [
    '-*-*-',
    '--*--',
    '----*',
    '*----'
]


# retorna un nuevo string con la casilla incrementada
def renovar_string(a_modificar, pos, value):
    """Recibe un string y remplaza el caracter en pos por value.

        Parametros:
            a_modificar : str
                El string que se va a modificar.
            pos : int
                Posición del caracter a modificar.
            value : str
                El valor a colocar en a_mdificar[pos].
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

        Para incrementar utiliza el método renovar_string.
        Este método se encarga de llamarlo con los valores necesarios.

        Parámetros:
            tablero : list,
                El tablero a modificar.
            linea_casilla : int
                Linea dónde se encuentra la casilla.
            pos_x_casilla : int
                Posición de la casilla en la linea.
    """
    # obtiene el valor a darle a la casilla
    valor_casilla_incrementada = str(
            int(tablero[linea_casilla][pos_x_casilla]) + 1
        )
    # actualiza el string
    tablero[linea_casilla] = renovar_string(
            tablero[linea_casilla],
            pos_x_casilla,
            valor_casilla_incrementada
        )


def incrementar_linea(tablero, linea_mina, pivot):
    """Incrementa la cantidad de minas en pivot - 1, pivot, pivot + 1.

        Verifica que existan casillas a izquierda/derecha del pivot.
        Verifica que ninguna tenga una mina.

        Parámetros:
            tablero : list
                El tablero a modificar.
            linea_mina : int
                Línea del tablero que se va a modificar.
            pivot : int
                A partir de donde se buscan las casillas a izq/der.
    """
    # si hay casilla a la izquierda y no es una mina
    if pivot - 1 >= 0 and tablero[linea_mina][pivot - 1] is not '*':
        incrementar_casilla(tablero, linea_mina, pivot - 1)

    # si hay casilla a la derecha y no es una mina
    if pivot + 1 < len(tablero[linea_mina]):
        if tablero[linea_mina][pivot + 1] is not '*':
            incrementar_casilla(tablero, linea_mina, pivot + 1)

    # si el 'pivot' no es una mina
    if tablero[linea_mina][pivot] is not '*':
        incrementar_casilla(tablero, linea_mina, pivot)


def incrementar_minas(tablero, linea_mina, pos):
    """Incrementa en 1 las casillas alrededor de una mina.

        Recibe la posición de la mina en el tablero y:
            * Verifica los límites arriba/abajo.
            * Llama al método incrementar_linea como corresponda.

        Parámetros:
            tablero : list
                El tablero a modificar.
            linea_mina : int
                Linea donde está la mina.
            pos : int
                Casilla de la línea dónde está la mina
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
    """Modifica el tablero, remplazando '-' por '0'.

        Facilita la utilización del método 'incrementar_casilla'.
        Evita que las casillas sin minas alrededor queden en '-'.

        Parámetros:
            tablero : list
                El tablero a modificar.
    """
    # recorre cada línea
    for i in range(len(tablero)):
        # el string de la línea es actualizado
        tablero[i] = tablero[i].replace('-', '0')


def contar_minas(tablero):
    """Modifica el tablero para que cada casilla muestre el número de minas alrededor.

        Parámetros:
            tablero : list
                El tablero a modificar.
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
    """Imprime el tablero en forma de matriz.

        Parámetros:
            tablero : list
                El tablero a imprimir.
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
