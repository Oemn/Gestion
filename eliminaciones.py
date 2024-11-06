import json
import os
def eliminacion_guardar(name_a ,db_eliminacion):
    with open (name_a, "w") as db:
        json.dump(db_eliminacion, db, indent = 4)