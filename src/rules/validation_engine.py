from rules.

class ValidationEngine:

    def __init__(self):

        self.rules = [

            MissingRecordRule(),

            FileExistenceRule(),

            RevisionRule(),

            DuplicateRule(),

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