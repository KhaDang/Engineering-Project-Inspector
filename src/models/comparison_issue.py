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

class FileMatching(ComparisonIssue):
    @property
    def message(self):
        return "Files Matching" # Normally it is not an issue :)


class RevisionMismatch(ComparisonIssue):

    @property
    def message(self):
        return "Revision mismatch"

class RevisionMatching(ComparisonIssue):

    @property
    def message(self):
        return "Revision matching"
