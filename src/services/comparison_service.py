import pandas as pd
# Import Models
from models.comparsion_result import ComparisonResult


class ComparisonService:
    def __init__(self,
                 validator_engines):
        self.validator = validator_engines

    def compare(
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

    def create_report(self, results, columns):
        report = []
        if len(results)>0:
            for drawing in results:
                if len(columns) == 5:
                    report.append(drawing.to_table_row())
                if len(columns) == 4:
                    report.append(drawing.to_table_row_rev())

        df = pd.DataFrame(report, columns=columns)
        df.to_excel("exported_dataframe.xlsx", index=False)


