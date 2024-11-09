import pandas as pd
from gestion_estudiantes import *
from datos_estudiantes import *
from gestion_cursos import *
from Calificaciones import *
from gestion_universidad import *
from eliminaciones import *
estudiantes=cargar_estudiantes()
cursos=("Filosofia", "Teologia", "Antropologia", "Arqueologia")
sede=("Concepcion","Lota")
while True:
    try:
        print("""
        1-Estudiantes
        2-Cursos
        3-Notas
        4-Universidad
        5-Promediar nota
        6-Listar alumnos y cursos
        7.Listar Estudiantes
        8-Cerrar programa
        """)
        menu=int(input("Introduzca opcion:  "))
        if menu == 1:
            while True:
                try:
                    print("""
                    1° Registrar
                    2° Eliminar
                    3° Volver menu
                    """)
                    opcion_estudiante=int(input("Seleccione opcion: "))
                    if opcion_estudiante == 1:
                        estudiantes.append(registrar_estudiante(estudiantes))
                        guardar_estudiantes(estudiantes)
                        break
                    elif opcion_estudiante == 2:
                        eliminar_estudiantes(estudiantes)
                        guardar_estudiantes(estudiantes)
                        break
                    elif opcion_estudiante == 3:
                        break
                    else:
                        print("Opcion ingresada invalida")
                except:
                    print("Valor ingresado incorrecto.")
                    
        elif menu == 2:
            while True:
                try:
                    print("""
                    1° Asignar curso
                    2° Listar cursos
                    3° Volver menu
                    """)
                    opcion_curso=int(input("Seleccione una opcion: "))
                    if opcion_curso == 1:
                        asignar_curso(estudiantes, cursos)
                        guardar_estudiantes(estudiantes)
                        break
                    elif opcion_curso == 2:
                        listar_cursos(cursos)
                        break
                    elif opcion_curso == 3:
                        break
                    else:
                        print("Opcion ingresada invalida.")
                except:
                    print("Valor ingresado incorrecto.")
        elif menu == 3:
            while True:
                try:
                    print("""
                    1° Asignar nota
                    2° Modificar nota
                    3° Eliminar nota(todas)
                    4° Salir
                    """)
                    opcion_nota=int(input("Seleccione opcion: "))
                    if opcion_nota == 1:
                        break
                    elif opcion_nota == 2:
                        break
                    elif opcion_nota == 3:
                        break
                    elif opcion_nota == 4:
                        break
                    else:
                        print("Opcion ingresada invalida.")
                except:
                    print("Valor ingresado incorrecto.")
        elif menu == 4:
            while True:
                try:
                    print("""
                    1° Asignar sede
                    2° Listar sede
                    3° Salir
                    """)
                    opcion_universidad=int(input("Seleccione opcion: "))
                    if opcion_universidad == 1:
                        asignar_sede(estudiantes)
                        guardar_estudiantes(estudiantes)
                        break
                    elif opcion_universidad == 2:
                        listar_sede(sede)
                        break
                    elif opcion_universidad == 3:
                        break
                    else:
                        print("Opcion ingresada invalida")
                except:
                    print("Valor ingresado incorrecto.")
        elif menu == 5:
            #promediar las notas(un solo estudiante)
            break
        elif menu == 6:
            break
        elif menu == 7:
            listar_estudiantes(estudiantes)
        elif menu == 8:
            guardar_estudiantes(estudiantes)
            print("Hasta la proximaaaaaaaaaaaaaaaa")
            break
        else:
            print("Opcion ingresada incorrecta. ")
    except:
        print("Valor ingresado incorrecto.")