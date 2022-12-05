from commands import *
from config import Config
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Button, Header, Footer, Static
from subprocess import PIPE

class NamespacesWidget(Static):
    """A Namespaces widget."""

    def compose(self, id = None, *args, **kwargs) -> ComposeResult:
        """Create child widgets of namespaces."""
        #self.id = id
        contenedor = Container()
        cabecera = Static("Namespaces")
        cabecera.styles.text_align = "center"
        contenedor.mount(cabecera)
        
        ns = get_namespaces()
        for namespace in ns:
            contenedor.mount(
                Button(id=namespace, label=namespace, name=Config.NAMESPACE_BUTTON_NAME, classes=Config.NAMESPACE_BUTTON_CLASS)
            )

        yield contenedor


class PodsWidgets(Static):
    """A Pods widget."""""

    def compose(self) -> ComposeResult:
        """Create child widgets of pods."""
        #self.id = id
        cabecera = Static("Pods")
        cabecera.styles.text_align = "center"
        
        self.contenedor = Container()
        self.contenedor.mount(cabecera)
        
        yield self.contenedor



class LogsWidget(Static):
    container = ""
    pod = ""


class KUIAppUI(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"),("q", "button_exit", "Exit"),("p","new_plots", "Plots"),("t","new_terminal","New Terminal")]
    CSS_PATH = "../styles.css"


    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        
        self.podsWidget = PodsWidgets()
        self.logsWidget = LogsWidget() 
        
        yield Container(
            NamespacesWidget(renderable="namespaces", id = "namespaces_widget"), 
            self.podsWidget, 
            self.logsWidget,
            id = "main_window"
        )
        

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_button_exit(self) -> None:   
        """An action to exit."""        
        self.exit()

    def action_new_plots(self) -> None:
        """An action to open plots."""
        subprocess.run("gnome-terminal -- bash -c '/bin/python3 /mnt/c/Users/abrah/Desktop/KUIApp/kuiapp/plots; exec bash -i'",stdout=PIPE,stderr=PIPE,shell=True)

    def action_new_terminal(self) -> None:
        """An action to open a new CL."""
        subprocess.run("gnome-terminal -- bash",stdout=PIPE,stderr=PIPE,shell=True)


    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        button_type = event.button.name

        if button_type == "btn_namespace":
            button_label = event.button.id
            namespaces = get_pods_names(button_label)

            # Clean any already existing buttons on the container
            for widget in self.podsWidget.contenedor.query("Button"):
                widget.remove()

            # Create buttons with the corresponding associated namespaces. 
            # They have to be added to the Pods container.

            for pod_name in namespaces:
                self.podsWidget.contenedor.mount(
                    Button(label=pod_name)
                )

            


if __name__ == "__main__":
    get_pods_names("")
    app = KUIAppUI()
    
    app.run()
    