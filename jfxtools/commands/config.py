import click
from jfxtools.settings import set


@click.command()
@click.argument("path", type=click.Path(exists=True))
def scenebuilder(path):
    """Ruta del .exe de SceneBuilder en su equipo"""
    set("pathSceneBuilder", path)


@click.command()
@click.argument("sufix")
def sufixcontroller(sufix):
    """Sufijo que se añadirá al nombre del controlador"""
    set("sufixControllers", sufix)