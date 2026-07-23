from rules.missing_record_rule import MissingRecordRule
from rules.revision_rule import RevisionRule
from rules.duplicate_rule import DuplicateRule

class ValidationEngine:

    def __init__(self):

        self.rules = [

            MissingRecordRule(),

            # FileExistenceRule(),

            RevisionRule(),

            # DuplicateRule(),

        ]

    def validate(
            self,
            left,
            right,
            result
    ):
        for rule in self.rules:
            rule.evaluate(
                left,
                right,
                result
            )