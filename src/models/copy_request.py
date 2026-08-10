from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

@dataclass
class CopyRequest:

    source : str
    extensions: list[str]
    destination: str
    copy_mode: Any

    lookup_list: list[str] = None
    overwrite: bool = False
    #
    # overwrite: bool


from dataclasses import dataclass
@dataclass
class CopyResult:

    copied: list[Path]
    skipped: list[Path]
    duplicates: list[str]
    failed: list[str]