def incorporación(**args):
    nombre = input('Ingresá el nombre del nuevo integrante: ')
    equipo = int(input('Ingresá a qué equipo querés integrarlo. 1 o 2: '))
    if equipo == 1:
        args['e' + str(equipo)].append(nombre)
    else:
        args['e' + str(equipo)].append(nombre)


equipos = {
    'e1': ['Juan', 'Pedro'],
    'e2': ['Ana']
}

resp = input('¿Deseas incorporar un integrante a algún equipo?. S/N: ')

if resp.upper() == 'S':
    incorporación(**equipos)

print('Los equipos con la incorporación quedaron conformados de la siguiente manera:')
print(f"Equipo 1: {equipos['e1']} - Equipo 2:{equipos['e2']}")
