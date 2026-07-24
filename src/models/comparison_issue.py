from abc import ABC
from abc import abstractmethod


class ComparisonIssue(ABC):

    @property
    @abstractmethod
    def message(self):
        pass


class MissingInLeft(ComparisonIssue):

    @property
    def message(self):
        return "Missing in Left"


class MissingInRight(ComparisonIssue):

    @property
    def message(self):
        return "Missing in Right"

class Match(ComparisonIssue):
    @property
    def message(self):
        return "Matching" # Normally it is not an issue :)


class RevisionMismatch(ComparisonIssue):

    @property
    def message(self):
        return "Revision mismatch"