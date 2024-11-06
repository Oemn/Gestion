# Colocar en un futuro los import
# import json
# from gestion_estudiantes import *
# estudiantes = dict()
# while True:
#     print('''
#         1°- Registrar Estudiantes
#         2° - Listar Estudiantes                 
#         3° - Modificar informacion
#         4° - Eliminar
#         5° - Obtener Promedio de un estudiante
#         6° - Cerrar Programa
#         ''')
#     opcion = int(input("Ingrese alguna de las opciones disponibles: "))
#     if opcion == 1:
#         añadir un menu de en que registrar si estudiantes ,curso
#         continue        
#     elif opcion == 2:
#         añadir menu si listar estudiantes solamente, + notas , +establecimiento
#         pass        
#     elif opcion == 3:
#         añadir si modificar notas, estudiantes, (nose que mas)
#         pass
#     elif opcion == 4:
#         Añadir si eliminar un curso , estudiante , notas , asignatura
#         pass
#     elif opcion == 5:
#         break
#     elif opcion == 6:
#         break
import pandas as pd
from gestion_estudiantes import *
from datos_estudiantes import *
from gestion_cursos import *
from Calificaciones import *
from add_new_course import *
from gestion_universidad import *
from datos_universidad import *
from eliminaciones import *
estudiantes=[]
cursos=[]
while True:
    print("""
    1-Registrar Estudiantes
    2-Modificar Estudiantes
    3-Eliminar Estudiantes
    4-Listar Estudiantes
    5-Registrar Cursos
    6-Modificar Cursos
    7-Eliminar Cursos
    8-Listar Cursos
    9-Modificar Calificacion //de esto no estoy seguro si hacerlo asi
    10-Asignar Calificacion //de esto no estoy seguro si hacerlo asi
    11-Calcular Promedio // En el documento no pide ver si el alumno esta aprobado o no asi que no lo haré
    12-Total alumnos y cursos
    13-Listar alumnos y cursos correspondientes
    14-Listar TODO
    15-Cerrar programa
    """)
    menu=int(input("Seleccione "))
    if menu == 1:
            estudiantes.append(registrar_estudiante(estudiantes))
            print(estudiantes)
    elif menu == 3:
        eliminar_estudiantes(estudiantes)
    if menu == 2:
        break
    if menu == 3:
        break
    if menu == 4:
        listar_estudiantes(estudiantes)
    if menu == 5:
        break
    if menu == 6:
        break
    if menu == 7:
        break
    if menu == 8:
        break
    if menu == 9:
        break
    if menu == 10:
        break
    if menu == 11:
        break
    if menu == 12:
        break
    if menu == 13:
        break
    if menu == 14:
        break
    if menu == 15:
        break
    else:
        print("Ingrese una opcion correcta.")