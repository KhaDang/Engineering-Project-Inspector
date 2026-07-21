
from models.parsed_filename import ParsedFileName
from pathlib import Path
import re


class FileNameParser:
    PATTERNS = [

        r"^(?P<number>.+)-(?P<revision>[A-Z])$",

        r"^(?P<number>.+)_(?P<revision>\d+\.\d+)$",
    ]

    def parse(self, filepath: str) -> ParsedFileName:

        path = Path(filepath)

        filename = path.stem

        extension = path.suffix.lower()

        for pattern in self.PATTERNS:

            match = re.match(pattern, filename)

            if match:
                return ParsedFileName(

                    filename=filename,

                    drawing_number=match.group("number"),

                    revision=match.group("revision"),

                    extension=extension
                )

        return ParsedFileName(

            filename=filename,

            drawing_number=filename,

            revision=None,

            extension=extension
        )