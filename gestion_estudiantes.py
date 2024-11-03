# def registro_estudiante():
#     Nombre = input("Ingrese Primer Nombre del Estudiante: ")
#     Apellido = input("Ingrese Primer Apellido del Estudiante: ")
#     Rut = int(input("..."))
#     matricula = id(Rut)
#     return Nombre, Apellido, Rut, matricula
estudiantes = dict()
cant = int(input("Cuantos estudiantes desea crear: "))
for i in range(0,cant):
    Nombre = input("Ingrese Primer Nombre del Estudiante: ")
    Apellido = input("Ingrese Primer Apellido del Estudiante: ")
    Rut = int(input("..."))
    matricula = id(Rut)
    estudiantes["est" + str(i)] = (Nombre, Apellido, Rut, matricula)
    
print(estudiantes)