from rules.base_rule import BaseRule
# Import from Models
from models.comparison_issue import RevisionMismatch

class RevisionRule(BaseRule):

    def evaluate(
        self,
        left,
        right,
        result
    ):

        if left is None or right is None:
            return

        if left.pdf_revision != right.pdf_revision:

            result.add_issue(
                RevisionMismatch()
            )