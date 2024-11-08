def listar_cursos(cursos):
    for i in range(len(cursos)): 
        print(f"Cursos:{cursos[i]}")
def modificar_cursos(cursos):
    pass
def asignar_curso(estudiantes, cursos):
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
            