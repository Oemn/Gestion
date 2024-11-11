import pandas as pd
from eliminaciones import *
db_eliminacion = []
def registrar_estudiante(estudiantes):
    loop=True
    existe=False
    while True:
        Nombre_c = input("Ingrese Nombre: ")
        if bool(Nombre_c) == False:
            continue
        else:
            break
    while loop:
        try:
            Rut = int(input("Ingrese rut (sin puntos,ni guion): "))
            for i in range(len(estudiantes)):
                if Rut == estudiantes[i]['Estudiante'][1]:
                    print("Ya existe el rut.")
                    existe=True
                    break#si existe rompe el bucle FOR con el break, para que asi en la siguiente iteracion no cambie el valor de existe a =False y pase
                else:
                    existe=False
            if existe == False:
                break
        except:
            print("Valor ingresado incorrecto.")
    for e in range(len(estudiantes)+1001): matricula = f"N°{e}"
    return {
        "Estudiante" : (Nombre_c, Rut, matricula), "Curso" : [] , "Sede": " "
    }
def eliminar_estudiantes(estudiantes, calificaciones):
    if bool(estudiantes):
        while True:
            borrar=int(input("Ingrese matricula estudiante: "))
            for i in range(len(estudiantes)):
                for estudiante in estudiantes:
                    if estudiante["Estudiante"][2] == f"N°{borrar}": 
                        db_eliminacion.append({
                        "Informacion Eliminada" : estudiantes.pop(i),
                        "Procendencia" : "Estudiantes"
                        },)
                        eliminacion_guardar(db_eliminacion)
                        print("Estudiante eliminado correctamente")
                        if f"N°{borrar}" in calificaciones:
                            db_eliminacion.append({
                                "informacion Eliminada" : calificaciones.pop(f"N°{borrar}"),
                                "Procendencia" : "Calificaciones"
                            })
                            eliminacion_guardar(db_eliminacion)
                        return
                    else:
                            print("Estudiante no encontrado.")
                            break
    else:
        print("No existen actualmente estudiantes creados, intentelo nuevamente en otra ocasion")
def listar_estudiantes(estudiantes):
    if bool(estudiantes):
        df = pd.DataFrame(data = estudiantes)
        df["Nombre"] = df["Estudiante"].str[0]
        df["Rut"] = df["Estudiante"].str[1]
        df["Matricula"] = df["Estudiante"].str[2]
        df = df.reindex(columns = ["Matricula","Nombre","Rut","Curso", "Sede"])
        return print(df)
    else:
        print("No existen estudiantes registrados.")