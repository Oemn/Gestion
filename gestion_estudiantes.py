def registro_estudiante():
    Nombre = input("Ingrese Primer Nombre del Estudiante: ")
    Apellido = input("Ingrese Primer Apellido del Estudiante: ")
    Rut = int(input("..."))
    matricula = id(Rut)
    return Nombre, Apellido, Rut, matricula

est2 = ("John smith", id(1), "11.111.111-1")
est3 = ("NN NN", id(2), "22.222.222-2")
est4 = ("aa aa", id(3), "33.333.333-3")
est5 = ("bb bb", id(4), "44.444.444-4")
est6 = ("cc cc", id(5), "55.555.555-5")
est7 = ("dd dd", id(6), "66.666.666-6")
est8 = ("ee ee", id(7), "77.777.777-7")
est9 = ("ff ff", id(8), "88.888.888-8")
est10 = ("gg gg", id(9), "99.999.999-9")
    
for i in range(2,10):
    print(est{i})