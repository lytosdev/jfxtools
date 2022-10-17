import click
import jfxtools.commands.config as cmdsconfig
import jfxtools.commands.create as cmdscreate
from jfxtools.common import open_fxml


@click.group()
def main():
    """App de ayuda para trabajar con JavaFX"""


@main.group()
def config():
    """Edita la configuración"""


@main.group()
def create():
    """Genera documentos"""


@main.command()
@click.argument("path")
def ofxml(path):
    """Abre un archivo .fxml con Scene Builder"""
    open_fxml(path)


config.add_command(cmdsconfig.scenebuilder)
config.add_command(cmdsconfig.sufixcontroller)
create.add_command(cmdscreate.main)
create.add_command(cmdscreate.sca)