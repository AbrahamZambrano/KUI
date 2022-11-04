from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
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


class NamespacesWidget(Static):
    """A Namespaces widget."""
    def compose(self) -> ComposeResult:
        """Create child widgets of namespaces."""
        yield Static("Namespaces", id="namespacesMessage")
        for namespace in get_namespaces():
            yield Button(namespace, id=namespace)



def get_pods(contenedor: str) -> str:
    pods = subprocess.run(["kubectl", "get", "pods", "-n", contenedor], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
    return pods



class PodsWidgets(Static):
    """A Pods widget."""""


class KUIAppUI(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    CSS_PATH = "styles.css"


    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        self.podsWidget = PodsWidgets("", id="podsWidget") 
        yield Container(NamespacesWidget(renderable="namespaces"), self.podsWidget)

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        container = event.button.id
        pod_info = get_pods(container)
        self.podsWidget.update( pod_info)




if __name__ == "__main__":
    app = KUIAppUI()
    namespace = NamespacesWidget()
    app.run()
    