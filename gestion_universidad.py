# def asignar_sede(estudiantes):
#     asignar=input("Ingresar matricula de estudiante: ")
#     sede_ingresar=input("Ingrese Sede a asignar: ")
#     for i in range(len(estudiantes)):
#         if f"N°{asignar}" == estudiantes[i]['Estudiante'][2]:
#             estudiantes[i]['Sede']=sede_ingresar
def asignar_sede(estudiantes,sede):
    while True:
        try:
            matricula=int(input("Ingrese matricula estudiante: "))
            for est in range(len(estudiantes)):
                if f"N°{matricula}" == estudiantes[est]['Estudiantes'][2]:
                    break
                else:
                    print("Estudiante no encontrado, intente nuevamente")
            break
        except:
            print("Valor ingresado incorrecto, intente nuevamente")
    print("Las sedes disponibles son las siguientes: ")
    print("1- Concepcion")
    print("1- Lota")
    sede_asignar=int(input("Seleccione opcion: "))
    if sede_asignar == 1:
        for i in range(len(estudiantes)):
            if f"N°{matricula}" == estudiantes[i]['Estudiante'][2]:
                estudiantes[i]['Sede']="Concepcion"
    elif sede_asignar == 2:
        for i in range(len(estudiantes)):
            if f"N°{matricula}" == estudiantes[i]['Estudiante'][2]:
                estudiantes[i]['Sede']="Lota"       
        
def listar_sede(sede):
    for i in range(len(sede)):
        print(f"Sede:{sede[i]}")
def eliminar_sede(sede):
    pass