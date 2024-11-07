import pandas as pd
from eliminaciones import *


def registrar_estudiante(estudiantes):

        Nombre_c = input("Ingrese Nombre: ")
        Rut = int(input("Ingrese rut (sin puntos,ni guion: )"))
        for e in range(len(estudiantes)+1001): matricula = f"N°{e}"
        return {
            "Estudiante" : (Nombre_c, Rut, matricula), "Curso":"","Notas":"","Sede":""
        }
    #se tendria que modificar la nota del estudiante
def eliminar_estudiantes(estudiantes):
    while True:
        borrar=int(input("Ingrese matricula estudiante: "))
        for i in range(len(estudiantes)):
            for estudiante in estudiantes:
                if estudiante["Estudiante"][2] == f"N°{borrar}": 
                    db_eliminacion = {
                    "Informacion Eliminada" : estudiantes.pop(i),
                    "Procendencia" : "Estudiantes"
                    }
                    eliminacion_guardar(db_eliminacion)
                    print("Estudiante eliminado correctamente")
                    return
                else:
                        print("Estudiante no encontrado.")
def listar_estudiantes(estudiantes):
    df = pd.DataFrame(data = estudiantes)
    return print(df.rename(columns = {"Estudiante" : "Informacion Estudiante", "Curso" : "Asignaturas a cursar"}))