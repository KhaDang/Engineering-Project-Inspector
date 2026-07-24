from rules.base_rule import BaseRule
# Import model

from models.comparison_issue import MissingInLeft, MissingInRight, Match


class MissingRecordRule(BaseRule):

    def evaluate(
        self,
        left,
        right,
        result
    ):

        if left and right:
            result.add_issue(Match())

        if left is None:

            result.add_issue(
                MissingInLeft()
            )

        elif right is None:

            result.add_issue(
                MissingInRight()
            )