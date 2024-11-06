import pandas as pd
# from gestion_cursos import *
# def registrar_estudiante(estudiantes):
#     cant = int(input("Cuantos estudiantes desea crear: "))
    
#     for i in range(len(estudiantes)+1,cant+(len(estudiantes))+1):
        
#         Nombre = input("Ingrese Primer Nombre del Estudiante: ")
#         Apellido = input("Ingrese Primer Apellido del Estudiante: ")
#         Rut = int(input("Ingrese rut (sin puntos,ni guion: )"))
#         for i in range(len(estudiantes)+100): matricula = f"N°{i}""
#         estudiantes["est" + str(i)] = (Nombre, Apellido, Rut, matricula)
#         asignaturas()

#     print(estudiantes)

def listar_estudiantes(estudiantes):
    df = pd.DataFrame(data = estudiantes)
    return print(df.rename(columns = {0 : "Nombre", 1 : "Rut" , 2 : "Matricula"},))
def registrar_estudiante(estudiantes):

        Nombre_c = input("Ingrese Primer Nombre y apellido del Estudiante: ")
        Rut = int(input("Ingrese rut (sin puntos,ni guion: )"))
        for e in range(len(estudiantes)+100): matricula = f"N°{e}"
        return {
            "Estudiante" : (Nombre_c, Rut, matricula)
        }
def modificar_nota_estudiantes(estudiantes):
    matricula_ver=int(input("Ingrese matricula de estudiante a modificar"))
    #se tendria que modificar la nota del estudiante
    pass
def eliminar_estudiantes(estudiantes):
    borrar=int(input("Ingrese Rut estudiante"))
    for i in estudiantes:
        if borrar == i['Rut']:
            #antes de eliminar lo añadimos al respaldo db_sys
            estudiantes.remove(i)
            print("Estudiante eliminado correctamente")
    
    print("Estudiante no encontrado.")
# def listar_estudiantes(estudiantes):
#     # for i in estudiantes:
#     #     print(f"Nombre: {i['Nombre']} Rut {i['Rut']} Matricula {i['Matricula']}")
#     # pass
    
