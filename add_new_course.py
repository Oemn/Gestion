def crear_curso(cursos):
    curso_crear=input("Ingrese nombre de curso: ")
    if curso_crear in cursos:
        print("El curso ya existe")
    else:
        cursos.append(curso_crear)
        print("Curso creado correctamente.")