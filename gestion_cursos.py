def listar_cursos(cursos):
    for i in range(len(cursos)): 
        print(f"Cursos:{cursos[i]}")
def asignar_curso(estudiantes, cursos):
    if bool(estudiantes):
        buscar = int(input("Ingrese la matricula del estudiante a asignar: "))
        for e in range(len(estudiantes)):
            if f"N°{buscar}" == estudiantes[e]["Estudiante"][2]:
                    for i in range(len(cursos)): 
                        print(f"Cursos:{cursos[i]}")
                    print("Estos son las Asignaturas disponibles actualmente")
                    asig = int(input("Ingrece el curso a asignar. Ej: Filosofia = 1 o arqueologia = 4"))
                    asig -= 1
                    estudiantes[e]["Curso"].append(cursos[asig])
                    break
            else: 
                print("Ingrese una matricula apropiada")
    else:
        print("No existen estudiantes.")