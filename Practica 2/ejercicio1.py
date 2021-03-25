with open('Practica 2\\numpy_readme.txt', 'r') as numpy_readme:
    print('Imprimiendo todas las líneas que contienen "http" o "https"')
    for line in numpy_readme:
        if 'http' in line or 'https' in line:
            print(line, end=" ")