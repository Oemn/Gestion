import pandas as pd
import json
import os
import datetime
from eliminaciones import *
db_c = []
def asignar_notas(estudiantes, calificaciones):
    while True:
        try:
            buscar_mat = int(input("Ingrese la matricula del estudiante ha asignar: "))
            for estudiante in estudiantes:
                if estudiante["Estudiante"][2] == f"N°{buscar_mat}":
                    if f"N°{buscar_mat}" not in calificaciones:   
                        calificaciones[f"N°{buscar_mat}"] = {}
                            
                    for c in estudiante["Curso"]:
                        if c not in calificaciones[f"N°{buscar_mat}"]:
                            calificaciones[f"N°{buscar_mat}"][c] = []
                                
                        elif c in calificaciones[f"N°{buscar_mat}"]:
                            continue
                            
                        print(f"Se ingresaran las calificaciones a la asignatura {c}")
                        for e in range(1,4):
                            while True:
                                try:    
                                    nota = float(input(f"Ingrese calificacion N°{e}: "))
                                    if nota >=1 and nota <=7:
                                        calificaciones[f"N°{buscar_mat}"][c].append(nota)
                                        break
                                    else:
                                        print("Ingrese calificacion en el range requerido: entre 1.0 y 7.0 ")
                                except:
                                    print("Valor ingresado incorrecto")        
                    return
        except:
            print("Valor ingresado incorrecto")                

def listar_calificaciones(calificaciones):
    if bool(calificaciones):
        print(pd.DataFrame(calificaciones).transpose())
    else:
        print("No se encuentran notas registradas.")
    
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
                now = str(datetime.datetime.now())
                db_c = {
                        "informacion Eliminada" : calificaciones.pop(f"N°{borrar}"),
                        "Procendencia" : "Calificaciones",
                        "Fecha de eliminacion" : now
                            }
                eliminacion_guardar(db_c)
                print("Calificacion/es eliminada correctamente.")
                return
            else:
                print("Estudiantes no encontrado.")

def modificar_calificaciones(cf):
    pass                   
                    
def promediar(calificaciones):
    found = False
    while True:
        matricula = int(input("Ingrese la matricula del estudiante: "))
        for key in calificaciones:
            if key == f"N°{matricula}":
                found = True
                for c in calificaciones[key]:
                    prom = 0
                    for i in range(0,3):
                        prom += calificaciones[key][c][i]
                    print(f"El Promedio de {c} es", prom/3)
        return
def modificar_calificaciones(calificaciones):
    while True:
        try:
            matricula = int(input("Ingrese la matrícula del estudiante para modificar notas: "))
            matricula_key = f"N°{matricula}"
            if matricula_key not in calificaciones:
                print("Estudiante no encontrado. Intente nuevamente.")
                continue
            print(f"Asignaturas disponibles para el estudiante {matricula_key}:")
            asignaturas = list(calificaciones[matricula_key].keys())# se usa para obtener todas las llaves de un diccionario
            for i, asignatura in enumerate(asignaturas, start=1):
                print(f"{i}. {asignatura}")

            while True:
                try:
                    opcion = int(input("Seleccione el número de la asignatura que desea modificar: ")) - 1
                    if opcion < 0 or opcion >= len(asignaturas):
                        print("Opción inválida. Intente nuevamente.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")

            asignatura_seleccionada = asignaturas[opcion]
            nuevas_notas = calificaciones[matricula_key][asignatura_seleccionada].copy() # .copy crea una copia de las notas actuales de la asignatura ingresada
            for i in range(3):
                nota_actual = nuevas_notas[i] if i < len(nuevas_notas) else None
                mensaje = f"Ingrese la nueva calificación N°{i+1} para {asignatura_seleccionada} (actual: {nota_actual}): "
                    
                while True:
                    entrada = input(mensaje)
                    if entrada == "":  #si ta vacia queda la nota anterior
                        break
                    try:
                        nota = float(entrada)
                        if 1.0 <= nota <= 7.0:
                            if i < len(nuevas_notas):
                                nuevas_notas[i] = nota
                            else:
                                nuevas_notas.append(nota)  # Añadir la nota si no existe
                            break
                        else:
                            print("Calificación fuera del rango permitido (1.0 - 7.0).")
                    except ValueError:
                        print("Valor ingresado incorrecto, ingrese un numero.")

            calificaciones[matricula_key][asignatura_seleccionada] = nuevas_notas # reemplaza las notas antiguas por las nuevas.
            print(f"Calificaciones de {asignatura_seleccionada} para el estudiante {matricula_key} actualizadas a {nuevas_notas}.")
            guardar_calificaciones(calificaciones)
            break

        except ValueError:
            print("Valor ingresado incorrecto.")