def es_heterograma(palabra):
    caracteres = {}
    
    for car in palabra:
        if not car in caracteres:
            caracteres[car] = 1
        else:
            return False
    return True


palabra = input('palabra: ')

if es_heterograma(palabra):
    print('heterograma')
else:
    print('no heterograma')
