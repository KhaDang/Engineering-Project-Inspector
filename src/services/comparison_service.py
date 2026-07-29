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



