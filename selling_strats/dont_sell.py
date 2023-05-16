from selling_strats.selling_strategy_base import SellingStrategyBase
from constants import API
from time import sleep
from position import Position
from datetime import datetime

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


# Never sell... Ever...
class DontSellTilNextDay(SellingStrategyBase):
    def __init__(self):
        super().__init__(sell_by_eod=False)

    def update(self, position: Position):
        if position.sell_order:
            return
        diff = datetime.now() - position.order_filled_time
        if diff.total_seconds() > 12 *60*60: # (12 hours)
            position.sell_order = API.submit_order(
                symbol=position.stock.data["symbol"],
                qty=position.qty,
                side="sell",
                type="market",
                time_in_force="day",
            )