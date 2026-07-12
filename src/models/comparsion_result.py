from dataclasses import dataclass

from models.drawing_record import DrawingRecord

@dataclass
class ComparisonResult:
    drawing_number: str
    left_record: DrawingRecord | None
    right_record: DrawingRecord | None
    status: str

