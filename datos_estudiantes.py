import json
import os
def obtener_estudiantes(estudiantes):
    with open("registro_gestion.json", "w") as gestion:
        json.dump(estudiantes, gestion, indent=4)
        return
def cargar_estudiantes():
    if os.path.exists("registro_gestion.json"):
        with open("registro_gestion.json", "r") as gestion:
            return json.load(gestion)
    else:
        print("No existe un archivo .json, asi que se creara uno nuevo")
        return []
