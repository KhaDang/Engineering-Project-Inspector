from dataclasses import dataclass, field
from models.drawing_record import DrawingRecord

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

    issues:list = field(default_factory=list)

    # status: ComparisonStatus

    def to_table_row(self):
        source = self.right_record or self.left_record

        return (
            self.drawing_number,
            "✓" if source and source.part_path else "X",
            "✓" if source and source.drawing_path else "X",
            "✓" if source and source.assembly_path else "X",
            ', '.join(issue.message for issue in self.issues)
        )

    def add_issue(self, issue):
        self.issues.append(issue)

    def has_issue(self, issue_type):
        return any(
            isinstance(issue, issue_type)
            for issue in self.issues
        )

    def to_table_row_rev(self):

        bom_revision = self.left_record.bom_revision if self.left_record and self.left_record.bom_revision else '-'
        pdf_revision = self.right_record.pdf_revision if self.right_record and self.right_record.pdf_revision else '-'
        return (
            self.drawing_number,
            bom_revision,
            pdf_revision,
            ', '.join(issue.message for issue in self.issues)
        )

    def to_table_row_fol(self):
        file_in_a = "✓" if self.left_record and self.left_record.drawing_number else 'X'
        file_in_b = "✓" if self.right_record and self.right_record.drawing_number else 'X'
        return (
            self.drawing_number,
            file_in_a,
            file_in_b,
            ', '.join(issue.message for issue in self.issues)
        )