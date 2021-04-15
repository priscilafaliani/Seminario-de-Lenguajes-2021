import csv

# abro el dataset
with open('Clase 5\\netflix_titles.csv', encoding='utf-8') as data_set:
    reader = csv.reader(data_set, delimiter=',')
    
    # creo el archivo .csv de salida
    with open('Clase 5\\titulos2020.csv', 'w', encoding='utf-8') as salida:
        writer = csv.writer(salida)
        
        # pongo el encabezado
        writer.writerow(reader.__next__())
        
        # escribo sólo los titulos estrenados en 2020
        writer.writerows(filter(lambda titulo: titulo[7] == '2020', reader))