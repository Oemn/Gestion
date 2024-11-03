def registrar_estudiante(estudiantes):
    cant = int(input("Cuantos estudiantes desea crear: "))
    for i in range(len(estudiantes)+1,cant+(len(estudiantes))+1):
        
        Nombre = input("Ingrese Primer Nombre del Estudiante: ")
        Apellido = input("Ingrese Primer Apellido del Estudiante: ")
        Rut = int(input("Ingrese rut (sin puntos,ni guion)"))
        matricula = f"N°{id(Rut)}"
        estudiantes["est" + str(i)] = (Nombre, Apellido, Rut, matricula)
        
    print(estudiantes)

def listar_estudiantes(estudiantes):
    for i in range(len(estudiantes)):
        print(estudiantes[i])
def modificar_estudiantes():
    pass
