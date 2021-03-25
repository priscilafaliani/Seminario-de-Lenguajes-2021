import string

def leer_letra():
    """Lee de consola hasta que el usuario ingrese una letra"""
    letra = input('letra: ')

    while letra not in string.ascii_letters:
        print('ingrese una letra...')
        letra = input('letra: ')
    
    return letra



texto = input('texto: ')

letra = leer_letra()

# obtengo las palabras
texto = texto.split(' ')

for palabra in texto:
    if palabra.startswith(letra):
        print(palabra)