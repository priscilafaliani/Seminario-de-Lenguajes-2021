from alumnos import nombres_a, nombres_b
from alumnos import nombres, evaluacion1, evaluacion2


def obtener_lista(str):
    """Retorna una lista a partir de un string, del cuál obtiene cada dato sin comillas"""
    return str.replace("'", "").split(", ")


def interseccion(nombres_a, nombres_b):
    """Retorna los valores que aparecen en ambas listas"""
    return [nombre for nombre in dict([(nombre, '') for nombre in nombres_a if nombre in nombres_b])]


def obtener_lista(str):
    """Retorna una lista a partir de un string, del cuál obtiene cada dato sin comillas"""
    return str.replace("'", "").split(", ")


def obtener_suma_notas(eval1, eval2):
    """Retorna una lista con forma  [(str(alumno), int(nota)), ..., ....]"""
    return [int(eval1[i]) + int(eval2[i]) for i in range(len(eval1))]


def obtener_notas_y_alumnos(nombres, eval1, eval2, total):
    """Retorna una lista del estilo [(str(alumno), int(eval1), int(eval2), int(total)), ..., ....]"""
    return list(zip(nombres, eval1, eval2, total))
    

def imprimir_alumno(codigo, datos):
    """Imprime un tuple de tipo (nombre, nota1, nota2, total)"""
    print(f'{codigo}\t{datos[0]}\t\t{datos[1]}\t\t{datos[2]}\t\t{datos[3]}')


def imprimir_alumnos(alumnos):
    print(f'\tNombre\t\tEval1\t\tEval2\t\tTotal')
    for i in range(len(alumnos)):
        imprimir_alumno(i, alumnos[i])

nombres_a = obtener_lista(nombres_a)
nombres_b = obtener_lista(nombres_b)

print('Nombres que existen en ambas listas: ', end=' ')
print(interseccion(nombres_a, nombres_b))

evaluacion1 = obtener_lista(evaluacion1)
evaluacion2 = obtener_lista(evaluacion2)

notas = obtener_notas_y_alumnos(obtener_lista(nombres), evaluacion1, evaluacion2, obtener_suma_notas(evaluacion1, evaluacion2))

imprimir_alumnos(notas)
