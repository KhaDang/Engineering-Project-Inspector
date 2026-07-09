from dataclasses import dataclass

@dataclass
class DrawingRecord:
    number: str
    rev: str
    has_part: bool = False
    has_drawing: bool = False
    has_assembly: bool = False
    has_pdf: bool = False
    has_step: bool = False
    status: str = ""