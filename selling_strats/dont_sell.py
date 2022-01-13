from selling_strats.selling_strategy_base import SellingStrategyBase
from constants import API
from time import sleep
from position import Position


# Simply do not sell until the end of the day.
class DontSellTilEOD(SellingStrategyBase):
    def update(self, position: Position):
        if position.sell_order:
            return
        sleep(1)  # do nothing


# Never sell... Ever...
class NeverSell(SellingStrategyBase):
    def __init__(self):
        super().__init__(sell_by_eod=False)

    def update(self, position: Position):
        if position.sell_order:
            return
        sleep(1)  # do nothing
