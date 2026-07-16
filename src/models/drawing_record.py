from dataclasses import dataclass, field

@dataclass
class DrawingRecord:

    drawing_number: str
    revision: str | None = None
    part_path: str | None = None
    part_duplicates: list[str] = field(default_factory=list)

    drawing_path: str | None = None
    drawing_duplicates: list[str] = field(default_factory=list)

    assembly_path: str | None = None
    assembly_duplicates: list[str] = field(default_factory=list)

    pdf_path: str | None = None
    pdf_duplicates: list[str] = field(default_factory=list)

    step_path: str | None = None

    def to_table_row(self):
        return (
            self.drawing_number,
            "✓" if self.part_path else "",
            "✓" if self.drawing_path else "",
            "✓" if self.assembly_path else "",
            "Ready"
        )