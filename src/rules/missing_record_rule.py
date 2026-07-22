from rules.base_rule import BaseRule

class MissingRecordRule(BaseRule):

    def evaluate(
        self,
        left,
        right,
        result
    ):

        if left is None:

            result.add_issue(
                MissingInLeft()
            )

        elif right is None:

            result.add_issue(
                MissingInRight()
            )