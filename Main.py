#Colocar en un futuro los import
import json
from gestion_estudiantes import *
import pandas as pd

estudiantes = dict()
while True:
    print('''
        1°- Registrar Estudiantes
        2° - Listar Estudiantes                 
        3° - Modificar informacion
        4° - Obtener Promedio de un estudiante
        5° - Cerrar Programa
        ''')
    opcion = int(input("Ingrese alguna de las opciones disponibles: "))
    if opcion == 1:
        registrar_estudiante(estudiantes)
        continue        
    elif opcion == 2:
        listar_estudiantes(estudiantes)
        pass        
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        break
