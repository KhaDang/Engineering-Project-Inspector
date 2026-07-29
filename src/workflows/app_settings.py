from dataclasses import dataclass, field

import json
from pathlib import Path

from dataclasses import asdict

@dataclass
class Settings:

    theme: str = "flatly"

    window_width: int = 1200

    window_height: int = 800

    recent_projects: list[str] = field(default_factory=list)

    @classmethod
    def load(cls):
        settings_file = Path("workflows/settings.json")
        if not settings_file.exists():
            return cls()

        with open(settings_file, "r") as file:
            data = json.load(file)
            return cls(**data)


    def save(self):
        settings_file = Path("workflows/settings.json")
        with open(settings_file, "w") as file:
            json.dump(
                asdict(self),

                file,

                indent=4

            )