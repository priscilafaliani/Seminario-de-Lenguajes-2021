from alumnos import nombres, evaluacion1, evaluacion2


def obtener_lista(str):
    """Retorna una lista a partir de un string, del cuál obtiene cada dato sin comillas"""
    return str.replace("'", "").split(", ")


def cargar_notas_finales(nombres, evaluacion1, evaluacion2):
    """Retorna un diccionario con la forma {str(nombre): int(nota_final)}"""
    return dict([(nombres[alumno], int(evaluacion1[alumno]) + int(evaluacion2[alumno])) for alumno in range(len(nombres))])


def calcular_promedio(notas):
    """Retorna el promedio de las notas de un dict con la forma {str(nombre): int(nota)}"""
    total = 0
    for alumno in notas:
        total += notas[alumno]
    return total / len(notas)


def no_superan_promedio(notas, promedio):
    """Retorna una lista con nombres de quienes no superan el promedio dado"""
    return [alumno for alumno in notas if notas[alumno] < promedio]


nombres = obtener_lista(nombres)
evaluacion1 = obtener_lista(evaluacion1)
evaluacion2 = obtener_lista(evaluacion2)

notas_finales = cargar_notas_finales(nombres, evaluacion1, evaluacion2)

print('Alumnos que no superan el promedio: ')
print(no_superan_promedio(notas_finales, calcular_promedio(notas_finales)))










