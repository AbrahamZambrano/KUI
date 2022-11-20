from commands import *
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Button, Header, Footer, Static


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

class PodRow(Static):
    def compose() -> ComposeResult:
        yield Button("coredns-565d847f94-4rspf")
        yield Static("1/1")
        yield Static("Running")
        yield Static("8 (68m ago)")
        yield Static("11d")




class PodsWidgets(Static):
    """A Pods widget."""""
    def compose(self, id = None, *args, **kwargs) -> ComposeResult:
        self.headers = Container(
            Static("NAME"),
            Static("READY"),
            Static("STATUS"),
            Static("RESTARTS"), 
            Static("AGE"),
            id = "pods_widget_header"
        )
        self.pods_rows = Container(
            # Los pods que tengas en total
            # PodRow(),
            
        )

        yield Container(self.headers, self.pods_rows,
        )



class LogsWidget(Static):
    container = ""
    pod = ""

class KUIAppUI(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    CSS_PATH = "../styles.css"
    NAMESPACE_BUTTON_CLASS = "button_namespaces"


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
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        id = event.button.id

        if KUIAppUI.NAMESPACE_BUTTON_CLASS in event.button.classes:
            pods = get_pods(id)
            #Converitr la lista en un string
            pods_list = ' '.join(map(str,pods))
            ########################################################
            self.podsWidget.pods_rows.add_class("remove")
            self.podsWidget.pods_rows.mount(Container(
                Static(pods_list), 
                id = "pods_row_container"
            )
        )

    #Intento de hacer un boton de exit
    class Exit(Static):
        """A button to exit"""
        def compose(self) -> ComposeResult:
            yield Button("Exit", id="exit")

if __name__ == "__main__":
    get_pods_names("")
    app = KUIAppUI()
    namespace = NamespacesWidget()
    app.run()
    