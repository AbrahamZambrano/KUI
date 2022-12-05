from commands import *
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
        contenedor.mount(Static("Namespaces"))
        
        ns = get_namespaces()
        for namespace in ns:
            contenedor.mount(
                Button(namespace, id=namespace, classes=KUIAppUI.NAMESPACE_BUTTON_CLASS)
            )

        yield contenedor


class PodsWidgets(Static):
    """A Pods widget."""""

    def compose(self, id = None, *args, **kwargs) -> ComposeResult:
        """Create child widgets of pods."""
        #self.id = id
        contenedor = Container()
        contenedor.mount(Static("Pods"))

        for pod in get_namespaces():
            ps = get_pods_names(pod)
            for pods in ps:
                btn = Button(pods, id=pods, classes=KUIAppUI.PODS_BUTTON_CLASS)
                btn.styles.visibility = "hidden"
                contenedor.mount(
                    btn
                )

        yield contenedor


class LogsWidget(Static):
    container = ""
    pod = ""

class KUIAppUI(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"),("e", "button_exit", "Exit"),("p","new_plots", "Plots"),("t","new_terminal","New Terminal")]
    CSS_PATH = "../styles.css"
    NAMESPACE_BUTTON_CLASS = "button_namespaces"
    PODS_BUTTON_CLASS = "button_pods"


    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        
        self.podsWidget = PodsWidgets("Pods", id="pods_widget")
        self.logsWidget = LogsWidget("Logs", id="logs_widget") 
        
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
        id = event.button.id

        if KUIAppUI.NAMESPACE_BUTTON_CLASS in event.button.classes:
            pods = get_pods_names(id)
            #Converitr la lista en un string
            pods_list = ' '.join(map(str,pods))
            ########################################################
            self.podsWidget.pods_rows.add_class("remove")
            self.podsWidget.pods_rows.mount(Container(
                Static(pods_list), 
                id = "pods_row_container"
            )
        )



if __name__ == "__main__":
    get_pods_names("")
    app = KUIAppUI()
    
    app.run()
    