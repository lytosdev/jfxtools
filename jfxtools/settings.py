import os
import json
import sys


path = os.path.join(os.path.dirname(sys.executable), "settings.json")


def get(key):
    settings = check()
    return settings[key]


def set(key, value):
    settings = check()
    settings[key] = value
    json.dump(settings, open(path, "w"))


def check():
    default_path_scenebuilder = "" if sys.platform != "win32" else rf"C:\Users\{os.getlogin()}\AppData\Local\SceneBuilder\scenebuilder.exe"
    if os.path.exists(path):
        settings = json.load(open(path))
        if "pathSceneBuilder" not in settings:
            settings["pathSceneBuilder"] = default_path_scenebuilder
        if "sufixControllers" not in settings:
            settings["sufixControllers"] = "Controller"
    else:
        settings = {"pathSceneBuilder": default_path_scenebuilder, "sufixControllers": "Controller"}
    json.dump(settings, open(path, "w"))
    return settings