import pandas as pd
from eliminaciones import *

def listar_estudiantes(estudiantes):
    df = pd.DataFrame(data = estudiantes)
    return print(df.rename(columns = {0 : "Nombre", 1 : "Rut" , 2 : "Matricula"},))
def registrar_estudiante(estudiantes):

        Nombre_c = input("Ingrese Primer Nombre y apellido del Estudiante: ")
        Rut = int(input("Ingrese rut (sin puntos,ni guion: )"))
        for e in range(len(estudiantes)+1001): matricula = f"N°{e}"
        return {
            "Estudiante" : (Nombre_c, Rut, matricula), "Curso":"","Notas":"","Sede":""
        }
    #se tendria que modificar la nota del estudiante
def eliminar_estudiantes(estudiantes):
    pass
    # while True:
    #     borrar=(input("Ingrese matricula estudiante: "))
    #     for key in estudiantes:
    #         for tupla in key:
    #             if borrar in tupla:
    #                 db_eliminacion = {
    #                 "Informacion Eliminada" : estudiantes.pop(tupla),
    #                 "Procendencia" : "Estudiantes"
    #                 }
    #                 print("Estudiante eliminado correctamente")
    #                 eliminacion_guardar(db_eliminacion)
    #             else:
    #                 print("Estudiante no encontrado.")
    #                 continue
# def listar_estudiantes(estudiantes):
#     # for i in estudiantes:
#     #     print(f"Nombre: {i['Nombre']} Rut {i['Rut']} Matricula {i['Matricula']}")
#     # pass
    
