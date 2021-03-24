"""Definición de funciones para resolver el desafio 4.

    Funciones:
        leer_notas()
            Retorna un diccionario de notas de alumnos.

        obtener_promedio(notas)
            Retorna el promedio entre notas de alumnos.

        obtener_alumnos_debajo_del_promedio(notas, promedio)
            Retorna los alumnos que no superan el promedio.

        imprimir_alumnos(alumnos)
            Imprime datos de alumnos con formato.
"""


def leer_notas():
    """Crea un diccionario con las notas y los nombres de estudiantes.

        Return:
            notas : dict
                {"nombre": nota, ...}
    """
    notas = {}

    nombre = input('nombre: ')
    while nombre != 'FIN':
        nota = int(input('nota: '))
        notas[nombre] = nota
        nombre = input('nombre: ')

    return notas


def obtener_promedio(notas):
    """Calcula el promedio entre las notas.

        Parámetros:
            notas : dict
                {"nombre": nota, ...}

        Return:
            promedio : float
    """
    total_notas = 0
    
    for alumno in notas:
        total_notas += notas[alumno]

    return total_notas / len(notas)


def obtener_alumnos_debajo_del_promedio(notas, promedio):
    """ Retorna un diccionario con los alumnos que no superan el promedio.

        Parámetros:
            notas : dict
                {"nombre": nota}
            
            promedio : float

        Return
            debajo_del_promedio : dict
                {"nombre": nota}
    """


    debajo_del_promedio = {}

    for alumno in notas:
        if notas[alumno] < promedio:
            debajo_del_promedio[alumno] = notas[alumno]

    return debajo_del_promedio


def imprimir_alumnos(alumnos):
    """Imprime los alumnos y sus notas con formato.

        Parámetros:
            alumnos : dict
                {"nombre": nota}
    """

    for alumno in alumnos:
        print(f'El alumno {alumno} obtuvo una nota de {alumnos[alumno]}')
        print('------------------------------------------------------')

