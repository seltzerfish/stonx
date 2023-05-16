from abc import abstractmethod, ABC
from copy import deepcopy
from datetime import datetime

# Abstract class.
class SourcingStrategy(ABC):
    def __init__(self, refresh_period_hours=1):
        self.cache = set()
        self.last_sourced = datetime.utcnow()
        self.refresh_period_hours = refresh_period_hours

    def source(self):
        diff = datetime.utcnow() - self.last_sourced
        if diff.total_seconds() / (60*60) > self.refresh_period_hours:
            self.cache = set()
        if self.cache:
            return self.cache
        self.cache = self.get_stocks()
        self.last_sourced = datetime.utcnow()
        return deepcopy(self.cache)

    @abstractmethod
    def get_stocks(self):
        pass

    def prepare(self):
        pass
