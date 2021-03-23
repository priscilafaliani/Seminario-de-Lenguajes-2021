""" 
Necesitamos procesar las notas de los estudiantes de este curso. Queremos saber:
    • cuál es el promedio de las notas;
    • cuántos estudiantes están por debajo del promedio
"""

notas = []

# lee notas hasta que se ingresa el -1
# suma las notas para luego calcular el promedio
nota = int(input('nota: (-1 para finalizar)'))
total_notas = 0
while nota != -1:
    notas.append(nota)
    total_notas += nota
    nota = int(input('nota: '))

# si se ingresó al menos una nota
if total_notas != 0:
    promedio = total_notas / len(notas)
    print(f'promedio: {promedio}')

    debajo_del_promedio = 0
    for nota in notas:
        if nota < promedio:
            debajo_del_promedio += 1

    print(f'estudiantes debajo del promedio: {debajo_del_promedio}')
else:
    print('no se ingresaron datos')