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
    def __init__(self, master, event: MenuBarEventHandler):

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


        self.menubar = tk.Menu(master)
        self.add_menu("File", FILE_MENU)
        self.add_menu("Edit", EDIT_MENU)
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


