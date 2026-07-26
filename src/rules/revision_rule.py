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
        left.bom_revision = self.normalize_revision(left.bom_revision)
        right.pdf_revision = self.normalize_revision(right.pdf_revision)

        if left.bom_revision == right.pdf_revision:
            result.add_issue(
                RevisionMatching()
            )

        if left.bom_revision != right.pdf_revision:

            result.add_issue(
                RevisionMismatch()
            )

    @staticmethod
    def normalize_revision(revision):

        if revision is None:
            return None

        revision = str(revision).strip()

        # Try numeric comparison
        try:
            number = float(revision)

            # 2.0 -> "2"
            if number.is_integer():
                return str(int(number))

            return str(number)

        except ValueError:
            pass

        # Text revisions (A, B, C...)
        return revision.upper()