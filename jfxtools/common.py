import os
import subprocess
from jfxtools.settings import get


def open_fxml(file_path):

    path = file_path if file_path.endswith(".fxml") else f"{file_path}.fxml"
    
    if os.path.exists(path):
        try:
            subprocess.Popen([get("pathSceneBuilder"), path])
        except:
            print("No se puede abrir el archivo, puede que la ruta de SceneBuilder sea incorrecta.")
            return False
    else:
        print("El archivo no existe")
        return False
    
    return True


class CodeByLine:

    code = []

    def __init__(self):
        self.clear()

    def add(self, line, ntab=0):
        self.code.append("    " * ntab + line)

    def clear(self):
        self.code.clear()

    def get_code(self):
        return "\n".join(self.code)