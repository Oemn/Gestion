def asignar_sede(estudiantes):
    if bool(estudiantes):
        encontrado = False
        loop=True
        while loop:
            try:
                matricula=int(input("Ingrese matricula estudiante: "))
                for i in range(len(estudiantes)):
                    if f"N°{matricula}" == estudiantes[i]['Estudiante'][2]:
                        encontrado=True
                        loop=False
                if encontrado == False:
                    print("Estudiante no encontrado.") 
            except:
                print("Valor ingresado incorrecto, intente nuevamente")
        print("Las sedes disponibles son las siguientes: ")
        print("1- Concepcion")
        print("2- Lota")
        loop=True
        while loop:
            try:
                sede_asignar=int(input("Seleccione opcion: "))
                if sede_asignar == 1:
                    for e in range(len(estudiantes)):
                        if f"N°{matricula}" == estudiantes[e]['Estudiante'][2]:
                            estudiantes[e]['Sede']="Concepcion"
                            loop=False
                elif sede_asignar == 2:
                    for e in range(len(estudiantes)):
                        if f"N°{matricula}" == estudiantes[e]['Estudiante'][2]:
                            estudiantes[e]['Sede']="Lota"
                            loop=False
                else:
                    print("Opcion Ingresada invalida")     
            except:
                print("Valor ingresado incorrecto.")
    else:
        print("No existen estudiantes")
def listar_sede(sede):
    print(f"Sede N°1: {sede[0]}\nSede N°2: {sede[1]}")
