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
    1- Estudiantes
    2- Cursos
    3- Calificaciones
    4- Total alumnos y cursos
    5- Listar Alumnos y cursos correspondientes
    6- Listar TODO
    7- Cerrar programa
""")
    menu_1=int(input("Seleccione opcion: "))
    if menu_1 == 1:
        print("""
              1- Registrar
              2- Modificar
              3- Eliminar
              """)
        opcion_estudiante=int(input("Seleccione una opcion: "))
        break
    if menu_1 == 2:
        print("""
              1- Registrar
              2- Modificar
              3- Eliminar
              """)
        opcion_cursos=int(input("Seleccione una opcion: "))
        break
    if menu_1 == 3:
        print("""
              1- Registrar
              2- Modificar
              3- Eliminar
              """)
        opcion_calificacion=int(input("Seleccione una opcion: "))
        break
    if menu_1 == 4:
        break
    if menu_1 == 5:
        break
    if menu_1 == 6:
        break
    if menu_1 == 7:
        break
    else:
        print("Ingrese una opcion correcta.")