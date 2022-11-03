from rich.table import Table

from textual.app import App, ComposeResult
from textual.widgets import Static
import delegator

class FizzBuzz(Static):
    def on_mount(self) -> None:
        namespaces_raw = delegator.run('kubectl get namespaces') 
        namespaces_info=namespaces_raw.out.split("\n")[1:]

        current_namespaces = list()
        for line in namespaces_info:
            current_namespaces.append(line.split(" ")[0])        
        

        table = Table("Namespaces", "Pods", "Logs")
        for namespace_name in current_namespaces:
            table.add_row(
                namespace_name,
                "      ",
                "      "
            )
        self.update(table)


class FizzBuzzApp(App):
    def compose(self) -> ComposeResult:
        yield FizzBuzz()


if __name__ == "__main__":
    app = FizzBuzzApp()
    app.run()
