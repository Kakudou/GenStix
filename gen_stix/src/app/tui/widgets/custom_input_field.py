from rich.align import Align
from rich.box import DOUBLE
from rich.console import RenderableType
from rich.panel import Panel
from rich.text import Text
from textual import events
from textual.reactive import Reactive
from textual.widget import Widget


class CustomInputField(Widget):

    title: Reactive[RenderableType] = Reactive("")
    content: Reactive[RenderableType] = Reactive("")

    def __init__(
        self,
        title: str,
        content: str = "",
        password: bool = False,
        placeholder: str = "",
        title_align: str = "center",
        auto_focus: bool = True,
        disabled: bool = False,
    ):
        self.can_focus = True
        super().__init__()
        self.title = title
        self.password = password
        self.content = content
        self.placeholder = placeholder
        self.prompt = ""
        self.title_align = title_align
        self.auto_focus = auto_focus
        self.disabled = disabled

    def on_key(self, event: events.Key) -> None:
        if not self.disabled:
            if event.is_printable:
                self.content += event.character
            elif event.key == "backspace":
                self.content = self.content[:-1]
            elif event.key == "enter" and self.auto_focus:
                self.app.action_focus_next()

    def watch_has_focus(self, value: bool) -> None:
        if value:
            self.prompt = "> "
        else:
            self.prompt = ""

    def on_paste(self, event: events.Paste) -> None:
        if not self.disabled:
            self.content += event.text

    def render(self) -> RenderableType:
        if self.content != "" or self.has_focus:
            if self.content is None:
                self.content = ""
            if self.password:
                renderable_text = Text(
                    f"{self.prompt}{'*' * len(self.content)}", style="bold"
                )
            else:
                renderable_text = Text(
                    f"{self.prompt}{self.content}", style="bold"
                )
        else:
            renderable_text = Text(
                f"{self.placeholder}",
                style="rgb(128,128,128) on rgb(50,57,50)",
            )
        renderable = Align.left(renderable_text)
        return Panel(
            renderable,
            title=self.title,
            title_align=self.title_align,
            height=3,
            style="bold white on rgb(50,57,50)",
            border_style="#004b6f",
            box=DOUBLE,
        )
