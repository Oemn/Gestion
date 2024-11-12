import json
import os
def eliminacion_guardar(db_eliminacion):
    newpath = './db_sys'
    if not os.path.exists(newpath):
        os.mkdir(newpath)
        print("Sea ha creado la carpeta db_sys")
        
    try:
        with open(os.path.join(newpath, "registro_eliminacion.json"), "r") as eliminar:
            registro = json.load(eliminar)
    except (FileNotFoundError, json.JSONDecodeError):
        registro = []
        
    registro.append(db_eliminacion)
    
    with open(os.path.join(newpath, "registro_eliminacion.json"), "w") as eliminar:
        json.dump(registro, eliminar, indent=4)
        
    return
