cadena = input('Ingresa la clave (debe tener menos de 10 caracteres y no contener los simbolos @ o !')

if len(cadena) > 10:
    print('Ingresaste mas de 10 caracteres')
elif '@' in cadena or '!' in cadena:
    print('Ingresaste algun simbolo @ o !')
else:
    print('Ingreso ok')
