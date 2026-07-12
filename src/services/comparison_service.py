from models.drawing_record import DrawingRecord
from models.comparsion_result import ComparisonResult

class ComparisonService:

    def compare(
        self,
        left_set: dict[str, DrawingRecord],
        right_set: dict[str, DrawingRecord]
    ):
        bom_keys = set(left_set)
        folder_keys = set(right_set)

        missing = bom_keys - folder_keys # only in BOM

        results = []

        for drawing in sorted(missing):
            record = left_set[drawing]
            results.append(
                ComparisonResult(
                    drawing_number=drawing,
                    left_record=record,
                    right_record=None,
                    status="Missing in Folder"
                )
            )
        return results




