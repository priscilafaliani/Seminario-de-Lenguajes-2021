def es_heterograma(palabra):
   return len(set(palabra)) == len(palabra) 

palabra = input('palabra: ')

if es_heterograma(palabra):
    print('heterograma')
else:
    print('no heterograma')
