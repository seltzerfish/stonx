from abc import abstractmethod, ABC
from copy import deepcopy

# Abstract class.
class SourcingStrategy(ABC):
    def __init__(self, refresh_period_hours=10):
        self.cache = set()
        self.refresh_period_hours = refresh_period_hours

    def source(self):
        if self.cache:
            return self.cache
        self.cache = self.get_stocks()
        return deepcopy(self.cache)

    @abstractmethod
    def get_stocks(self):
        pass

    def prepare(self):
        pass
