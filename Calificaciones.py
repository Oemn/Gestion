def asignar_notas(estudiantes):
    buscar = int(input("Ingrese la matricula del estudiante ha asignar: "))
    for i in range(len(estudiantes)):
        if estudiantes[i]["Estudiantes"][2] == f"N°{buscar}":
            print(estudiantes[i])
