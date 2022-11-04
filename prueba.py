from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Header, Footer, Static
import re
import subprocess

def get_namespaces():
    # Ejecutar comando de kubernetes para sacar el texto
    # Guardar el resultado en un array 

    namespaces = subprocess.run(["kubectl", "get", "namespaces"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    namespaces = namespaces.replace("\n", " ")
    namespaces = namespaces.replace("24h", " ")
    namespaces = namespaces.replace("Active", " ")
    res = re.findall(r"[a-z0-9](?!.*--)[a-z0-9-]{1,61}[a-z0-9]", namespaces)
    
    return res


class TimeDisplay(Static):
    """A widget to display elapsed time."""

class Stopwatch(Static):
    """A stopwatch widget."""

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        for namespace in get_namespaces():
            yield Button(namespace)

class StopwatchApp(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Container(Stopwatch())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = StopwatchApp()
    
    namespace = Stopwatch()
    app.run()
    