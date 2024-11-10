def listar_cursos(cursos):
    print(f"Asignaturas: {cursos[0]} {cursos[1]} {cursos[2]} {cursos[3]}")

def asignar_curso(estudiantes, cursos):
    found = False
    while True:
        if bool(estudiantes):
            buscar = int(input("Ingrese la matricula del estudiante a asignar: "))
            for e in range(len(estudiantes)):
                if f"N°{buscar}" == estudiantes[e]["Estudiante"][2]:
                    found = True
                    if found == False:
                        print("Matricula no encontrada")
                        continue
                    for i in range(len(cursos)): 
                        print(f"Cursos:{cursos[i]}")
                    print("Estos son las Asignaturas disponibles actualmente")
                    asig = int(input("Ingrece el curso a asignar. {Ej}: Filosofia = 1 o arqueologia = 4 : ")) - 1
                    curso_asig = cursos[asig]
                    if curso_asig in estudiantes[e].get("Curso", []):
                            print("Este curso ya se encuentra asignado.")
                            continue
                    else:
                        estudiantes[e]["Curso"].append(curso_asig)
                        print(f"Curso '{curso_asig}' asignado exitosamente a {estudiantes[e]['Estudiante'][0]}.")
                        return
        else:
            print("No existen estudiantes.")