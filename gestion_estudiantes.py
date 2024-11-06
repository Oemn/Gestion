# import pandas as pd
# from gestion_cursos import *
# def registrar_estudiante(estudiantes):
#     cant = int(input("Cuantos estudiantes desea crear: "))
    
#     for i in range(len(estudiantes)+1,cant+(len(estudiantes))+1):
        
#         Nombre = input("Ingrese Primer Nombre del Estudiante: ")
#         Apellido = input("Ingrese Primer Apellido del Estudiante: ")
#         Rut = int(input("Ingrese rut (sin puntos,ni guion: )"))
#         matricula = f"N°{id(Rut)}"
#         estudiantes["est" + str(i)] = (Nombre, Apellido, Rut, matricula)
#         asignaturas()

#     print(estudiantes)

# def listar_estudiantes(estudiantes):
#     est_ordenados = pd.Dataframe(estudiantes)
#     return print(est_ordenados)
# def modificar_estudiantes():
#     pass
def registrar_estudiante(estudiantes):
    nombre=input("Ingrese nombre estudiante")
    rut=int("Ingrese rut estudiante")
    for i in range(len(estudiantes)+100): matricula = f"N°{i}"
    estudiante={"Nombre": nombre, "Rut": rut, "Matricula": matricula} # No estas guardando los datos como tupla, aunque por ahora no lo cambiare
    return (estudiante)
def modificar_estudiantes(estudiantes):
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
def listar_estudiantes(estudiantes):
    for i in estudiantes:
        print(f"Nombre: {i['Nombre']} Rut {i['Rut']} Matricula {i['Matricula']}")
    pass
