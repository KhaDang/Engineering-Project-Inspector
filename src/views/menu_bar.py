import sys
import tkinter as tk

from dataclasses import dataclass
from typing import Callable

@dataclass
class MenuBarEventHandler:
    on_export: Callable | None = None
    on_loadsettings: Callable | None = None
    on_clear: Callable | None = None


@dataclass
class MenuItem:

    label: str | None =  None
    command: Callable | None = None
    separator: bool = False
    accelerator: str = ""


class MenuBar:
    def __init__(self,
                 master,
                 event: MenuBarEventHandler,
                 update_theme=None):

        FILE_MENU = [

            MenuItem("New",event.on_loadsettings),
            MenuItem("Export", event.on_export),
            MenuItem(separator=True),
            MenuItem("Exit",on_exit),
        ]

        EDIT_MENU = [

            MenuItem("Clear", event.on_clear),
            MenuItem(separator=True),
            MenuItem("Copy", on_exit),
        ]

        THEMES = {

            "Flatly": "flatly",

            "Cosmo": "cosmo",

            "Superhero": "superhero",

            "Cyborg": "cyborg",

        }

        theme_menu = MenuItem()
        for label, theme in THEMES.items():
            theme_menu.command(

                label=label,

                command=lambda t=theme:
                self.on_theme_changed(t)

            )

        self.menubar = tk.Menu(master)
        self.add_menu("File", FILE_MENU)
        self.add_menu("Edit", EDIT_MENU)
        self.add_menu("Theme", THEMES)
        master.config(menu=self.menubar)


    def on_new_project():
        print("New Project pressed")

    def on_open(self):
        ...
    def add_menu(self,menu_label, menu_config):
        submenu = tk.Menu(self.menubar, tearoff=False)
        for item in menu_config:
            if item.separator:
                submenu.add_separator()
                continue
            submenu.add_command(label=item.label, command=item.command)
        self.menubar.add_cascade(label=menu_label ,menu=submenu)

def on_exit():
    sys.exit(0)


