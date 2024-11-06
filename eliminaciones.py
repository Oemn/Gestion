import json
import os
db_eliminacion ={}
def eliminacion_guardar(db_eliminacion):
    newpath = r'./db_sys'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    b = open("/db_sys/registro_eliminacion.json", "w")
    Informacion_a_guardar = json.dumps(db_eliminacion, indent=4)
    b.write(Informacion_a_guardar)
    b.close()
    return