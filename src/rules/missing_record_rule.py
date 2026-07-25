from rules.base_rule import BaseRule
# Import model

from models.comparison_issue import MissingInLeft, MissingInRight, FileMatching


class MissingRecordRule(BaseRule):

    def evaluate(
        self,
        left,
        right,
        result
    ):

        if left and right:
            result.add_issue(
                FileMatching()
            )

        if left is None:
            result.add_issue(
                MissingInLeft()
            )
        elif right is None:
            result.add_issue(
                MissingInRight()
            )