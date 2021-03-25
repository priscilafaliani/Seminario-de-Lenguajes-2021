palabras_frase = input('frase: ').lower().split(' ')

palabras = {}
for palabra in palabras_frase:
    if palabra in palabras:
        palabras[palabra] = palabras[palabra] + 1
    else:
        palabras[palabra] = 1

print([palabra for palabra in palabras.keys()])

