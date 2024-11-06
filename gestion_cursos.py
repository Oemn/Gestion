def listar_cursos(cursos):
    for i in range(len(cursos)): print(f"Cursos:{i[cursos]}")
    pass
def modificar_cursos(cursos):
    pass
def eliminar_cursos(cursos):
    #antes de eliminar lo añadimos al respaldo db_sys
    pass
def asignar_cursos(est, cursos):
    while True:
        buscar = int(input("Ingrese la matricula del estudiante a asignar: "))
        for i in range(len()):
            if f"N°{buscar}" == est[i]["estudiante"][2]:
                for i in range(len(cursos)): print(f"Cursos:{i[cursos]}")
                print("Estos son las Asignaturas disponibles actualmente")
                asig = int(input("Ingrece el curso a asignar. Ej: Filosofia = 1 o arqueologia = 4"))
                asig -= 1
                est[i]["cursos"] = cursos[asig]
            else: 
                print("Ingrese una matricula apropiada")