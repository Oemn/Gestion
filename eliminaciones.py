import json
import os
db_eliminacion ={}
def eliminacion_guardar(db_eliminacion):
    newpath = './db_sys'
    if not os.path.exists(newpath):
        os.mkdir(newpath)
        print("Sea ha creado la carpeta db_sys")
    with open(os.path.join(newpath, "registro_eliminacion.json"), "w") as b:
        Informacion_a_guardar = json.dumps(db_eliminacion, indent=4)
        b.write(Informacion_a_guardar)
    return
