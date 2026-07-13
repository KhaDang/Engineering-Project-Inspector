from models.drawing_record import DrawingRecord
from models.comparsion_result import ComparisonResult
from models.comparsion_result import ComparisonStatus


class ComparisonService:
    def __init__(self):
        ...
    def compare(
        self,
        left_set: dict[str, DrawingRecord],
        right_set: dict[str, DrawingRecord]
    ):
        # Combine all sets to one set of data
        all_keys = set(left_set) | set (right_set)
        results = []
        # Loop through all set and assign status, then store to results
        for drawing in sorted(all_keys):
            left = left_set.get(drawing)
            right = right_set.get(drawing)
            status = self.determine_status(left, right)

            results.append(
                ComparisonResult(
                    drawing_number=drawing,
                    left_record=left,
                    right_record=right,
                    status=status
                )
            )

        return results

    def determine_status(
            self,
            left: DrawingRecord | None,
            right: DrawingRecord | None
    ) -> ComparisonStatus:
        if left and right:
            return ComparisonStatus.MATCH
        if left:
            return ComparisonStatus.RIGHT_ONLY
        return ComparisonStatus.LEFT_ONLY

    def filter_results(
            self,
            results,
            excluded: set[ComparisonStatus]
    ):
        return [
            r for r in results
            if r.status not in excluded
        ]



