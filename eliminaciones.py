import json
import os
def eliminacion_guardar(db_eliminacion):
    with open ("db.json", "w") as db:
        json.dump(db_eliminacion, db, indent = 4)