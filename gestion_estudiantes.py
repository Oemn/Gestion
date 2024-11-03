def registrar_estudiante():
    estudiantes = dict()
    cant = int(input("Cuantos estudiantes desea crear: "))
    for i in range(0,cant):
        Nombre = input("Ingrese Primer Nombre del Estudiante: ")
        Apellido = input("Ingrese Primer Apellido del Estudiante: ")
        Rut = int(input("Ingrese rut (sin puntos,ni guion)"))
        matricula = id(Rut)
        estudiantes["est" + str(i)] = (Nombre, Apellido, Rut, matricula)
        print(estudiantes)

def listar_estudiantes(estudiantes):
    for i in range(len(estudiantes)):
        print(f"Nombre{estudiantes[i][0]} {estudiantes[i][1]} Rut {estudiantes[i][2]} Matricula {estudiantes[i][3]}")
def modificar_estudiantes():
    pass
