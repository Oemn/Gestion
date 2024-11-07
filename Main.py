import pandas as pd
from gestion_estudiantes import *
from datos_estudiantes import *
from gestion_cursos import *
from Calificaciones import *
from add_new_course import *
from gestion_universidad import *
from datos_universidad import *
from eliminaciones import *
import os
import json
estudiantes=cargar_estudiantes()
cursos=["Filosofia", "Teologia", "Antropologia", "Arqueologia"]
sede=[]
while True:
    print("""
    1-Estudiantes
    2-Cursos
    3-Notas
    4-Universidad
    5-Promediar nota
    6-Listar alumnos y cursos
    7-Listar TODO
    8.Listar Estudiantes
    9-Cerrar programa
    """)
    menu=int(input("Seleccione "))
    if menu == 1:
        print("""
        1-Registrar
        2-Modificar
        3-Eliminar
        """)
        opcion_estudiante=int(input("Seleccione opcion: "))
        if opcion_estudiante == 1:
            estudiantes.append(registrar_estudiante(estudiantes))
            obtener_estudiantes(estudiantes)
            continue
        
        if opcion_estudiante == 2:
            break
        if opcion_estudiante == 3:
            eliminar_estudiantes(estudiantes)
            continue
    elif menu == 2:
        print("""
        1-Crear curso
        2-Asignar curso
        3-Listar cursos
        """)
        opcion_curso=int(input("Seleccione una opcion: "))
        if opcion_curso == 1:
            crear_curso(cursos)
        if opcion_curso == 2:
            asignar_curso(estudiantes, cursos)
        if opcion_curso == 3:
            listar_cursos(cursos)
    elif menu == 3:
        print("""
        1-Asignar nota
        2-Modificar nota
        3-Eliminar nota(todas)
        """)
        opcion_nota=int(input("Seleccione opcion: "))
        if opcion_nota == 1:
            break
        if opcion_nota == 2:
            break
        if opcion_nota == 3:
            break
    elif menu == 4:
        print("""
        1-Crear sede
        2-Asignar sede
        3-Listar sede
        4-Eliminar sede
        """)
        opcion_universidad=int(input("Seleccione opcion: "))
        if opcion_universidad == 1:
            crear_sede(sede)
        if opcion_universidad == 2:
            asignar_sede(estudiantes)
        if opcion_universidad == 3:
            listar_sede(sede)
        if opcion_universidad == 4:
            break
    elif menu == 5:
        #promediar las notas(un solo estudiante)
        break
    elif menu == 6:
        break
    elif menu == 7:
        break
    elif menu == 8:
        listar_estudiantes(estudiantes)
        continue
    elif menu == 9:
        obtener_estudiantes(estudiantes)
        break