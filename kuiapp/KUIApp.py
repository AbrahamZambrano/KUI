from commands import *
from config import Config
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Button, Header, Footer, Static
from subprocess import PIPE

class NamespacesWidget(Static):
    """A Namespaces Widget."""

    def compose(self, id = None, *args, **kwargs) -> ComposeResult:
        """Create Child Widgets of Namespaces."""
        #self.id = id
        cabecera = Static("Namespaces")
        cabecera.styles.text_align = "center"
        cabecera.styles.background = "steelblue"
        
        contenedor = Container()
        contenedor.mount(cabecera)
        
        ns = get_namespaces()
        for namespace in ns:
            contenedor.mount(
                Button(id=namespace, label=namespace, name=Config.NAMESPACE_BUTTON_NAME, classes=Config.NAMESPACE_BUTTON_CLASS)
            )

        yield contenedor

class PodsWidget(Static):
    """A Pods Widget."""""

    def compose(self) -> ComposeResult:
        """Create Child Widgets of Pods."""
        #self.id = id
        cabecera = Static("Pods")
        cabecera.styles.text_align = "center"
        cabecera.styles.background = "palevioletred"
        
        self.contenedor = Container()
        self.contenedor.mount(cabecera)
        
        yield self.contenedor


class LogsWidget(Static):
    """A Logs Widget"""

    container = ""
    pod = ""

    def compose(self) -> ComposeResult:
        self.log_container = Static()
        cabecera = Static("Logs")
        cabecera.styles.text_align = "center"
        cabecera.styles.background = "darkslategray"
        yield cabecera
        yield self.log_container


class KUIAppUI(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"),("q", "button_exit", "Exit"),("p","new_plots", "Plots"),("t","new_terminal","New Terminal")]
    CSS_PATH = "../styles.css"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        
        self.podsWidget = PodsWidget()
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

        #Namespaces
        if button_type == Config.NAMESPACE_BUTTON_NAME:
            ns = event.button.id
            
            self.last_clicked_namespace = ns

            pods = get_pods_names(ns)

            # Clean any already existing buttons on the container
            for widget in self.podsWidget.contenedor.query("Button"):
                widget.remove()

            # Don´t forget to remove possible logs
            self.logsWidget.log_container.update()

            # Create buttons with the corresponding associated namespaces. 
            # They have to be added to the Pods container.

            for pod_name in pods:
                self.podsWidget.contenedor.mount(
                    Button(label=pod_name, id=pod_name, name=Config.PODS_BUTTON_NAME)
                )

        #Logs
        if button_type == Config.PODS_BUTTON_NAME :
            pod = event.button.id
            logs = get_logs(self.last_clicked_namespace, pod)
            self.logsWidget.log_container.update(logs)



if __name__ == "__main__":
    get_pods_names("")
    app = KUIAppUI()    
    app.run()
    