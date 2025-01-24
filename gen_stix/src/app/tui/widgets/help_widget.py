from textual.widget import Widget
from textual.app import ComposeResult
from textual.widgets import Markdown


class HelpWidget(Widget):

    HELP_MD = """
# GenSTIX Help

The usage of this application is simple.
When you highlight an item in the navigation tree on the left, you can use the following:

---

## On a **_Project name_** or **_"GenSTIX"_**:

- '`c`':
    Opens a form to create a new project.
- '`d`':
    Deletes the selected project and all associated data.

---

## On a **_type of STIX_** Object (e.g. 'Kill Chain Phase', 'Attack Pattern', 'MAC Address', etc.):

- '`c`':
    Opens a form to create a new object of the selected type.
- '`d`':
    Deletes all objects of the selected type.
- '`r`' or '`f`':
    Opens a form to search for objects of the selected type and print the results.

---

## On a **_STIX_** Object:

- '`c`':
    Opens a form to create a new object of the same type as the selected object.  
- '`a`' or 'enter':
    Shows the details of the selected object, along with its JSON representation.
- '`u`':
    Updates the selected object.
- '`d`':
    Deletes the selected object.

---

## General keys

- '`esc`' or '`q`':
    Clears the content part of the screen (the right side).
- '`h`':
    Displays this help screen.
- '`ctrl+c`':
    Exits the application.

---

# **Happy STIXing!**  
# ✨ Made with ❤️ by [Kakudou ~ カクドウ](https://kakudou.org)✨  
# ☕️ Feel free to contribute to [my daily coffee](https://www.buymeacoffee.com/Kakudou) ☕️  

---

"""  # noqa: W291

    def __init__(self, id, classes) -> None:
        super().__init__(id=id, classes=classes)

    def compose(self) -> ComposeResult:
        yield Markdown(self.HELP_MD)
