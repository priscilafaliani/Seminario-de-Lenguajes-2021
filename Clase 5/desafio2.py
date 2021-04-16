from collections import Counter
from functools import reduce
import csv


def get_paises_titulo(titulo):
    """Retorna una lista de los países productores de un título.
    
        Un título puede haber sido producido en 0 o más países.

        El índice 5 se corresponde con el campo 'country'
        de cada fila del dataset.
    """
    return titulo[5].split(', ') if titulo[5] else []


def print_resultados(paises):
    """Imprime con formato los resultados del análisis."""
    print('----- Top 5 países que realizaron más producciones -----')
    print()

    for i in range(5):
        nombre_pais = paises[i][0]
        producciones_totales = paises[i][1]
        print(f'{i + 1}) {nombre_pais}: {producciones_totales} producciones.')

    print()
    print('--------------------------------------------------------')


# abro el dataset
with open('Clase 5\\netflix_titles.csv', encoding='utf-8') as data_set:
    reader = csv.reader(data_set, delimiter=',')

    # obtengo la cantidad de títulos por país
    # el reduce se encarga de crear una única lista
    # de todas las listas.
    titulos_pais = Counter(reduce(lambda lista, pais: lista + pais, map(get_paises_titulo, reader), []))

    print_resultados(titulos_pais.most_common(5))
