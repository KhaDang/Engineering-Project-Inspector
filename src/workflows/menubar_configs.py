from dataclasses import dataclass
from email.iterators import body_line_iterator
from typing import Callable

@dataclass
class MenuItem:

    label: str | None =  None

    command: Callable | None = None

    is_enable: bool = True

    separator: bool = False
    accelerator: str = ""

class MenubarConfig:
    def __init__(self, blind_events):
        self.FILE_MENU = [

            MenuItem("Export Report", blind_events['on_export'], is_enable=False),
            MenuItem("Find missing files...", blind_events['on_popup'], is_enable=False),
            MenuItem(separator=True),
            MenuItem("Exit", blind_events['on_exit'], is_enable=True),
        ]

        self.EDIT_MENU = [

            MenuItem("Clear", blind_events['on_clear'], is_enable=False),
            MenuItem(separator=True),
            # MenuItem("Copy", on_exit),
        ]

        self.THEME_MENU = [
            # Light themes
            MenuItem("Flatly", command= lambda: blind_events['on_theme_changed']('flatly')),
            MenuItem("Cosmo",  command= lambda:blind_events['on_theme_changed']('cosmo')),
            MenuItem("Journal",  command= lambda:blind_events['on_theme_changed']('journal')),
            MenuItem("Litera",  command= lambda:blind_events['on_theme_changed']('litera')),
            MenuItem("Lumen",  command= lambda:blind_events['on_theme_changed']('lumen')),
            MenuItem("Simplex",  command= lambda:blind_events['on_theme_changed']('simplex')),
            MenuItem(separator=True),
            # Dark themes

            MenuItem("Darkly",  command= lambda:blind_events['on_theme_changed']('darkly')),
            MenuItem("Solar",  command= lambda:blind_events['on_theme_changed']('solar')),
            MenuItem("SuperHero",  command= lambda:blind_events['on_theme_changed']('superhero')),
            MenuItem("Vapor",  command= lambda:blind_events['on_theme_changed']('vapor')),
            MenuItem("Cyborg",  command= lambda:blind_events['on_theme_changed']('cyborg')),

        ]
