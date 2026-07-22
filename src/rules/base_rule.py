from abc import ABC
from abc import abstractmethod

class BaseRule(ABC):

    @abstractmethod
    def evaluate(
        self,
        left,
        right,
        result
    ):
        pass