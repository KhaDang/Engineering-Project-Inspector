from dataclasses import dataclass
from models.drawing_record import DrawingRecord

from enum import Enum
class ComparisonStatus(Enum):
    MATCH = 'Match'
    LEFT_ONLY = 'Missing in left'
    RIGHT_ONLY = 'Missing in right'

@dataclass
class ComparisonSummary:

    indexed_files: int
    bom_rows: int
    matches: int
    missing_left: int
    missing_right: int
    duplicates: int


@dataclass
class ComparisonResult:
    drawing_number: str
    left_record: DrawingRecord | None
    right_record: DrawingRecord | None
    status: ComparisonStatus

    def to_table_row(self):
        source = self.right_record or self.left_record

        return (
            self.drawing_number,
            "✓" if source and source.part_path else "X",
            "✓" if source and source.drawing_path else "X",
            "✓" if source and source.assembly_path else "X",
            self.status.value,
        )
