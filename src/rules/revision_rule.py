from rules.base_rule import BaseRule
# Import from Models
from models.comparison_issue import RevisionMatching, RevisionMismatch

class RevisionRule(BaseRule):

    def evaluate(
        self,
        left,
        right,
        result
    ):
        if left is None or right is None:
            return

        if left.bom_revision == right.pdf_revision:
            print(left.bom_revision)
            print(right.pdf_revision)
            print('------')
            result.add_issue(
                RevisionMatching()
            )

        if left.bom_revision != right.pdf_revision:

            result.add_issue(
                RevisionMismatch()
            )
