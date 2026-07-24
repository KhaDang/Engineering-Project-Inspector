import pandas as pd
# Import Models
from models.drawing_record import DrawingRecord
from models.comparsion_result import ComparisonResult

# Import rules, validation engine
from rules.validation_engine import ValidationEngine

class ComparisonService:
    def __init__(self):
        self.validator = ValidationEngine()

    def compare_validation(
            self,
            left_records,
            right_records
    ):

        all_keys = set(left_records) | set(right_records)

        results = []

        for drawing in sorted(all_keys):
            left = left_records.get(drawing)

            right = right_records.get(drawing)

            result = ComparisonResult(
                drawing_number=drawing,
                left_record=left,
                right_record=right
            )

            self.validator.validate(
                left,
                right,
                result
            )

            results.append(result)

        return results


    def compare(
        self,
        left_set: dict[str, DrawingRecord],
        right_set: dict[str, DrawingRecord],
        progress_callback=None
    ):
        # Combine all sets to one set of data
        all_keys = set(left_set) | set (right_set)

        results = []
        current = 0
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
            # Send the current to update progressbar
            current += 1
            if progress_callback:
                progress_callback(current)

        return results

    # def determine_status(
    #         self,
    #         left: DrawingRecord | None,
    #         right: DrawingRecord | None
    # ) -> ComparisonStatus:
    #     if left and right:
    #         return ComparisonStatus.MATCH
    #     if left:
    #         return ComparisonStatus.LEFT_ONLY
    #     return ComparisonStatus.RIGHT_ONLY

    def filter_results(
            self,
            results,
            excluded: set[DrawingRecord]
    ):
        return [
            r for r in results
            if r.status not in excluded
        ]

    def create_report(self, results):
        report = []
        if len(results)>0:
            for drawing in results:
                report.append(drawing.to_table_row())

        df = pd.DataFrame(report, columns=["Drawing", "SLDPRT", "SLDDRW", "SLDASM", "PDF", "STATUS"])
        df.to_excel("exported_dataframe.xlsx", index=False)



