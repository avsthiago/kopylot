import rich
from rich.panel import Panel
from rich.text import Text


def ai_print(header: str, result: str, no_color: bool = False, style: str = "bold green") -> str:
    if no_color:
        print("\n{header}:\n{text}")
    else:
        rich.print(
            Panel(
                Text(result),
                title=f"\U0001f916 {header}",
                style=style,
            )
        )
    return result
