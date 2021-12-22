from abc import abstractmethod, ABC
from position import Position


class SellingStrategyBase(ABC):
    def __init__(self, sell_by_eod=True):
        self.sell_by_eod = sell_by_eod

    def prepare(self):
        pass

    @abstractmethod
    def update(self, position):
        pass
