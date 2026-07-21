
from dataclasses import dataclass, field
@dataclass
class ParsedFileName:

    filename: str

    drawing_number: str

    revision: str | None

    extension: str

