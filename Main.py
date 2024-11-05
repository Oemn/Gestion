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
from gestion_estudiantes import *
from datos_estudiantes import *
from gestion_cursos import *
from Calificaciones import *
from add_new_course import *
from gestion_universidad import *
from datos_universidad import *
estudiantes=[]
cursos=[]
while True:
    print("""
    1-Registrar Estudiantes
    2-Modificar Estudiantes
    3-Eliminar Estudiantes
    4-Listar Estudiantes
    """)
    menu=int(input("Seleccione "))
    if menu == 1:
        break
    if menu == 2:
        break
    if menu == 3:
        break
    if menu == 4:
        break
    else:
        break