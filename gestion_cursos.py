def listar_cursos(cursos):
    for i in range(len(cursos)): 
        print(f"Cursos:{cursos[i]}")
def modificar_cursos(cursos):
    pass
def eliminar_cursos(cursos):
    #antes de eliminar lo añadimos al respaldo db_sys
    pass
def cursos_a(estudiantes, cursos):
    buscar = int(input("Ingrese la matricula del estudiante a asignar: "))
    for i in range(len(estudiantes)):
        if f"N°{buscar}" == estudiantes[i]["Estudiante"][2]:
            for i in range(len(cursos)): print(f"Cursos:{i[cursos]}")
            print("Estos son las Asignaturas disponibles actualmente")
            asig = int(input("Ingrece el curso a asignar. Ej: Filosofia = 1 o arqueologia = 4"))
            asig -= 1
            estudiantes[i]["cursos"] = cursos[asig]
            break
        else: 
            print("Ingrese una matricula apropiada")