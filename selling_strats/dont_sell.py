from selling_strats.selling_strategy_base import SellingStrategyBase
from constants import API
from time import sleep
from position import Position


# Simply do not sell.
class DontSell(SellingStrategyBase):
    def update(self, position: Position):
        if position.sell_order:
            return
        sleep(1)  # do nothing
        super().update(position)
