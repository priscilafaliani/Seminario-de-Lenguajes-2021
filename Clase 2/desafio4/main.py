"""Desafio muy similar al 3.

    Que cambió:
        * Usamos diccionarios. 
        * Usamos funciones para modularizar.
        * Se ingresa el nombre y la nota del estudiante.

    Qué hace:
        * Calcula el promedio de las notas
        * Indica que estudiantes están por debajo del promedio
"""

from manejo_alumnos import *

datos_alumnos = leer_notas()

promedio_notas = obtener_promedio(datos_alumnos)

debajo_del_promedio = obtener_alumnos_debajo_del_promedio(datos_alumnos, promedio_notas)

print('-------- ALUMNOS CON NOTA DEBAJO DEL PROMEDIO --------')
imprimir_alumnos(debajo_del_promedio)
