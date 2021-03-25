from alumnos import nombres, evaluacion1, evaluacion2


def obtener_lista(str):
    """Retorna una lista a partir de un string, del cuál obtiene cada dato sin comillas"""
    return str.replace("'", "").split(", ")


def obtener_suma_notas(eval1, eval2):
    """Retorna una lista con forma  [(str(alumno), int(nota)), ..., ....]"""
    return [int(eval1[i]) + int(eval2[i]) for i in range(len(eval1))]


def obtener_notas_y_alumnos(nombres, notas):
    return list(zip(nombres, notas))


def calcular_promedio(notas):
    """Retorna el promedio de las notas de una lista con forma [(str(alumno), int(nota))]"""
    total = 0
    for alumno in notas:
        total += alumno[1]
    return total / len(notas)


def no_superan_promedio(notas, promedio):
    """Retorna una lista con nombres de quienes no superan el promedio dado"""
    return [datos[0] for datos in notas if datos[1] < promedio]


notas = obtener_notas_y_alumnos(obtener_lista(nombres), obtener_suma_notas(obtener_lista(evaluacion1), obtener_lista(evaluacion2)))

print('Alumnos que no superan el promedio: ', end=' ')
print(no_superan_promedio(notas, calcular_promedio(notas)))