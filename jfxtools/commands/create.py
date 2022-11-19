import click
import os
from jfxtools.common import open_fxml, CodeByLine
from jfxtools.settings import get


@click.command()
@click.argument("name")
def main(name):
    """Crea la clase punto de entrada"""
    
    main_filename = f"{name}.java"
    
    if os.path.exists(main_filename):
        print(f"El archivo '{main_filename}' ya existe")
        return
    
    # Escribimos el main
    file = open(main_filename, "x")
    file.write(generate_main(name))
    file.close()


def generate_main(class_name):
    code = CodeByLine()
    code.add(f"package {os.path.basename(os.getcwd())};")
    code.add("")
    code.add("import java.io.IOException;")
    code.add("")
    code.add("import javafx.application.Application;")
    code.add("import javafx.fxml.FXMLLoader;")
    code.add("import javafx.scene.Parent;")
    code.add("import javafx.scene.Scene;")
    code.add("import javafx.stage.Stage;")
    code.add("")
    code.add(f"public class {class_name} extends Application {{")
    code.add("")
    code.add("@Override", 1)
    code.add("public void start(Stage primaryStage) throws IOException {", 1)
    code.add("")
    code.add("Parent root = FXMLLoader.load(getClass().getResource(\"MainScene.fxml\"));", 2)
    code.add("Scene scene = new Scene(root);", 2)
    code.add("primaryStage.setTitle(\"Hello World!\");", 2)
    code.add("primaryStage.setScene(scene);", 2)
    code.add("primaryStage.show();", 2)
    code.add("")
    code.add("}", 1)
    code.add("")
    code.add("public static void main(String[] args) {", 1)
    code.add("launch(args);", 2)
    code.add("}", 1)
    code.add("")
    code.add("}")
    return code.get_code()


@click.command()
@click.argument("name")
@click.option("-o", is_flag=True)
def sca(name, o):
    """Crea una vista y su controlador"""

    view_filename = f"{name}.fxml"
    sufix = get("sufixControllers")
    controller_name = f"{name}{sufix}"
    controller_filename = f"{controller_name}.java"

    if os.path.exists(view_filename):
        print(f"El archivo '{view_filename}' ya existe")
        return
    elif os.path.exists(controller_filename):
        print(f"El archivo '{controller_filename}' ya existe")
        return

    # Escribimos la vista
    file = open(view_filename, "x")
    file.write(generate_view(controller_name))
    file.close()

    # Escribimos el controlador
    file = open(controller_filename, "x")
    file.write(generate_controller(controller_name))
    file.close()

    # Abrimos el fxml creado
    if o:
        open_fxml(view_filename)


def generate_view(controller_name):
    code = CodeByLine()
    code.add("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
    code.add("")
    code.add("<?import javafx.scene.layout.AnchorPane?>")
    code.add("")
    code.add(f"<AnchorPane fx:id=\"pnl\" prefHeight=\"600.0\" prefWidth=\"1000.0\" xmlns=\"http://javafx.com/javafx/18\" xmlns:fx=\"http://javafx.com/fxml/1\" fx:controller=\"{os.path.basename(os.getcwd())}.{controller_name}\">")
    code.add("<!-- TODO Add Nodes -->", 1)
    code.add("</AnchorPane>")
    return code.get_code()


def generate_controller(controller_name):
    code = CodeByLine()
    code.add(f"package {os.path.basename(os.getcwd())};")
    code.add("")
    code.add("import java.net.URL;")
    code.add("import java.util.ResourceBundle;")
    code.add("")
    code.add("import javafx.fxml.FXML;")
    code.add("import javafx.fxml.Initializable;")
    code.add("import javafx.scene.layout.AnchorPane;")
    code.add("")
    code.add(f"public class {controller_name} implements Initializable {{")
    code.add("")
    code.add("@FXML", 1)
    code.add("private AnchorPane pnl;", 1)
    code.add("")
    code.add(f"public {controller_name}() {{", 1)
    code.add("")
    code.add("}", 1)
    code.add("")
    code.add("@Override", 1)
    code.add("public void initialize(URL arg0, ResourceBundle arg1) {", 1)
    code.add("")
    code.add("}", 1)
    code.add("")
    code.add("}")
    return code.get_code()