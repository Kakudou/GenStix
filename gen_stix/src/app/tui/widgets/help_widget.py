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
    Will open a form to create a new project.
- '`d`':
   Will delete the selected project and all its associated data.

---

## On a **_type of STIX_** Object (e.g. 'Indicator', 'Attack Pattern', 'MAC Address', etc.):

- '`c`':
   Will open a form to create a new object of the selected type.
- '`d`':
   Will delete all objects of the selected type.

---

## On a **_STIX_** Object:

- '`c`':
   Will open a form to create a new object of the same type as the selected object with the same properties as placeholders.
- '`a`' or 'enter':
   Will show the details of the selected object, and the json representation of the object.
- '`u`':
   Will update the selected object.
- '`d`':
   Will delete the selected object.
- '`p`':
   Will only output the json representation of the selected object.

---

## General keys

- '`q`':
   Will clear the content part of the screen, this mean the right part of the screen.
- '`h`':
   Will show this help screen.
- '`ctrl+c`':
   Will exit the application.

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
