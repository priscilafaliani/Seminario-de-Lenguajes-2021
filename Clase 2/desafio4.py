""" 
    Lo mismo que en el desafio 3 pero:
        * Usamos diccionarios. Se ingresa el nombre y la nota del estudiante.
        * Usamos funciones para modularizar.

    - cuál es el promedio de las notas
    + QUÉ estudiantes están por debajo del promedio
"""

# retorna un diccionario con las notas y los nombres de los estudiantes
def leer_notas():
    alumnos = {}

    nombre = input('nombre: ')
    while nombre != 'FIN':
        nota = input('nota: ')
        alumnos[nombre] = nota
        nombre = input('nombre: ')
    
    return alumnos

# recorre el diccionario (alumno: nota) y retorna el promedio de notas entre todos los alumnos
def obtener_promedio(notas):
    total_notas = 0
    
    for alumno in notas:
        total_notas += notas[alumno]

    return total_notas / len(notas)

# recorre el diccionario de (alumno: nota) y retorna otro diccionario con los alumnos que no superan el promedio (alumno: nota)
def obtener_alumnos_debajo_del_promedio(notas, promedio):
    debajo_del_promedio = {}

    for alumno in notas:
        if notas[alumno] < promedio:
            debajo_del_promedio[alumno] = notas[alumno]

    return debajo_del_promedio


