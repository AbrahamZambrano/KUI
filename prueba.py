from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Header, Footer, Static
import re
import subprocess

def get_namespaces() -> list:
    # Ejecutar comando de kubernetes para sacar el texto
    # Guardar el resultado en un array 

    #ejecutas el comando y obtienes el resultado en utf-8
    namespaces = subprocess.run(["kubectl", "get", "namespaces"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    
    #Parsea el resultado
    namespaces = re.sub("\s*[0-9]h", " ", namespaces)
    namespaces = namespaces.replace("\n", " ")
    namespaces = namespaces.replace("Active", " ")

    #Encuentra unicamente los nombres de los contenedores
    res = re.findall(r"[a-z0-9](?!.*--)[a-z0-9-]{1,61}[a-z0-9]", namespaces)
    
    return res


def pods(contenedor: str) -> str:
    pods = subprocess.run(["kubectl", "get", "pods", "-n", contenedor], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return pods


class NamespacesWidget(Static):
    """A stopwatch widget."""
    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        for namespace in get_namespaces():
            yield Button(namespace, id=namespace)


class KUIAppUI(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Container(NamespacesWidget())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        container = event.button.id
        pod_info = pods(container)




if __name__ == "__main__":
    app = KUIAppUI()
    namespace = NamespacesWidget()
    app.run()
    