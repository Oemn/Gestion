import pandas as pd
from eliminaciones import *
db_eliminacion = []
def registrar_estudiante(estudiantes):
    loop=True
    existe=False
    Nombre_c = input("Ingrese Nombre: ")
    while loop:
        try:
            Rut = int(input("Ingrese rut (sin puntos,ni guion: )"))
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
        "Estudiante" : (Nombre_c, Rut, matricula), "Curso": [],"Notas":"","Sede":""
    }
def eliminar_estudiantes(estudiantes):
    #revisar si existen estudiantes antes de hacerlo
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
                    return
                else:
                        print("Estudiante no encontrado.")
                        break
def listar_estudiantes(estudiantes):
    if bool(estudiantes):
        df = pd.DataFrame(data = estudiantes)
        return print(df.rename(columns = {"Estudiante" : "Informacion Estudiante", "Curso" : "Asignaturas a cursar"}))
    else:
        print("No existen estudiantes registrados.")