import pandas as pd
import json
import os
from eliminaciones import *
db_c = []
def asignar_notas( estudiantes, calificaciones):
        found = False
        for i in range(len(estudiantes)):
            buscar_mat = int(input("Ingrese la matricula del estudiante ha asignar: "))
            if estudiantes[i]["Estudiante"][2] == f"N°{buscar_mat}":
                if f"N°{buscar_mat}" not in calificaciones:   
                    calificaciones[f"N°{buscar_mat}"] = {}
                    
                for c in estudiantes[i]["Curso"]:
                    print(f"Se ingresaran las calificaciones a la asignatura {c}")
                    if c not in calificaciones[f"N°{buscar_mat}"]:
                        calificaciones[f"N°{buscar_mat}"][c] = []
                        
                    for e in range(1,4):
                        while True:    
                            nota = float(input(f"Ingrese calificacion N°{e}: "))
                            if nota > 0 and nota < 8 :
                                calificaciones[f"N°{buscar_mat}"][c].append(nota)
                                break
                            else:
                               print("Ingrese calificacion en el range requerido: entre 1.0 y 7.0 ")
                return                 
            elif found == False:
                print("Matricula no Encontrada")

def listar_calificaciones(calificaciones):
    print(pd.DataFrame(calificaciones).transpose())
    
def guardar_calificaciones(calificaciones):
        with open("calificaciones.json", "w") as n:
            json.dump(calificaciones, n, indent=4)
            return
def cargar_calificaciones():
        if os.path.exists("calificaciones.json"):
            with open("calificaciones.json", "r") as n:
                return json.load(n)
        else:
            print("No existe un archivo .json, asi que se creara uno nuevo")
            return {}
def eliminar_calificaciones(calificaciones):
    if bool(calificaciones):
        while True:
            borrar = int(input("Ingrese matricula estudiante: "))
            if f"N°{borrar}" in calificaciones:
                db_c.append({
                                "informacion Eliminada" : calificaciones.pop(f"N°{borrar}"),
                                "Procendencia" : "Calificaciones"
                            })
                eliminacion_guardar(db_c)
                print("Calificacion/es eliminada correctamente.")
                return
            else:
                print("Estudiantes no encontrado.")
                    