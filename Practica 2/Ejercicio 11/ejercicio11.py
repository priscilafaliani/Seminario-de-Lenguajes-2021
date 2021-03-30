from categorias import categorias
from string import ascii_letters


def contar_tabs_al_comienzo(categoria):
    """Retorna la cantidad de tabs al comienzo de un string"""
    tabs = 0
    espacios = 0
    for car in categoria:
        if car in ascii_letters:
            return tabs
        if car == ' ':
            espacios += 1
        if espacios == 4:
            tabs += 1
            espacios = 0
    return tabs


def parse_categorias(categorias):
    """Retorna un una lista a partir de un string de categorias.
    
        Parametros:
            categorias : str -> un texto con la forma:
                categoria1
                    subcategoria1
                    subcategoria2
                        subcategoria1
                        subcategoria2
                categoria2
                ...
                ...
            
        Return:
            list : [
                {'nombre': str(nombre_categoria), 'subcategorias': [
                    {(mismo tipo de dict)}, 
                    ...
                ]}, 
                ...
            ]
    """

    # separa el string en lineas
    categorias = categorias.split('\n')

    # donde se irá almacenando el resultado
    parsed = []

    # Pila utilizada para:
    #   Retornar niveles de las sublistas
    #   Agregar una categoria en la última categoria cargada
    categoria_actual = [parsed]

    # Nombre de la categoria anterior para comparaciones
    categoria_anterior = {'nombre': ''}

    for categoria in categorias:
        # ignora lineas en blanco
        if categoria:
            tabs_actual = contar_tabs_al_comienzo(categoria)
            tabs_anterior = contar_tabs_al_comienzo(categoria_anterior['nombre'])

            # el objeto que se va a guardar
            categoria_nueva = {'nombre': categoria, 'subcategorias': []}

            # si llegué a una subcategoria
            if tabs_actual > tabs_anterior:
                # guardo la referencia en la pila para volver después
                categoria_actual.append(categoria_anterior['subcategorias'])

            # si llegué al final de una subcategoria
            elif tabs_actual < tabs_anterior:
                # puede ser que tenga que retirar de la pila más de una categoria 
                # por ejemplo, en caso de que ocurra algo así:
                # [ 
                #  categoria1
                #       subcategoria1 -> el ultimo elemento en la pila es este
                #           subcategoria1
                #   categoria2 -> un solo pop me dejaría acá
                # -> pero necesito estar a este nivel ] 
                for i in range(tabs_anterior - tabs_actual):
                    categoria_actual.pop(len(categoria_actual) - 1)

            # actualizo el anterior (utilizado en caso de que tenga que agregar un nuevo elemento a la pila)
            categoria_anterior = categoria_nueva

            # guardo la categoria donde corresponde
            categoria_actual[len(categoria_actual) - 1].append(categoria_nueva)

    return parsed


def contar_subcategorias(categorias):
    """Recibe un dict de categorias. Retorna total de subcategorias.
    
        Parametros:
            dict -> {'nombre': str(), 'subcategorias' : list()}
    """

    total = len(categorias['subcategorias'])
    for categoria in categorias['subcategorias']:
        total = total + contar_subcategorias(categoria)
    return total


def imprimir_categorias(categorias):
    """Imprime las categorias principales + cantidad de subcategoria + cada una de ellas."""
    for i in range(len(categorias)):
        nombre = categorias[i]['nombre']
        if nombre.startswith(' '):
            print(' ' * contar_tabs_al_comienzo(nombre), end='')
            print(f'* {nombre.strip()}')
        else:
            print(f'----- {nombre.strip().upper()} -----')
            print(f'Subcategorias: {contar_subcategorias(categorias[i])}')
        imprimir_categorias(categorias[i]["subcategorias"])
            

imprimir_categorias(parse_categorias(categorias))
