def crear_sede(sede):
    sede_crear=input("Ingrese nombre de Sede")
    if sede_crear in sede:
        print("La sede ya existe")
    else:
        sede.append(sede_crear)
def asignar_sede(estudiantes):
    asignar=input("Ingresar matricula de estudiante: ")
    sede_ingresar=input("Ingrese Sede a asignar: ")
    for i in range(len(estudiantes)):
        if f"N°{asignar}" == estudiantes[i]['Estudiante'][2]:
            estudiantes[i]['Sede']=sede_ingresar
def listar_sede(sede):
    for i in range(len(sede)):
        print(f"Sede:{sede[i]}")
        
def eliminar_sede(sede):
    pass