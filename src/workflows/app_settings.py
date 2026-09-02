from dataclasses import dataclass, field

import json
from pathlib import Path
import sys

from dataclasses import asdict

@dataclass
class Settings:

    theme: str = "flatly"

    window_width: int = 1200

    window_height: int = 1200

    recent_projects: list[str] = field(default_factory=list)

    @classmethod
    def load(cls):

        settings_file = Path("src/workflows/settings.json")

        if not settings_file.exists():
            return cls()

        with open(settings_file, "r") as file:
            data = json.load(file)
            return cls(**data)


    def save(self):
        settings_file = self.get_resource_path("settings.json")
        with open(settings_file, "w") as file:
            json.dump(
                asdict(self),
                file,
                indent=4

            )

    def get_resource_path(self,relative_path) -> Path:
        """ Get absolute path to resource, works for dev and for PyInstaller """
        if hasattr(sys, "_MEIPASS"):
            base_path = Path(sys._MEIPASS)
        else:
            # app.py is located inside src
            base_path = Path(__file__).resolve().parent
        return base_path/ relative_path