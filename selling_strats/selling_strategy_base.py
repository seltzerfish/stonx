from abc import abstractmethod, ABC
from util.misc_util import market_closing_soon
from position import Position
from constants import API


class SellingStrategyBase(ABC):
    def __init__(self, sell_by_eod=True):
        self.sell_by_eod = sell_by_eod

    def prepare(self):
        pass

    @abstractmethod
    def update(self, position: Position):
        if not self.sell_by_eod or position.sell_order:
            return
        if market_closing_soon():

            print(
                "market will close soon. selling {}".format(
                    position.stock.data["symbol"]
                )
            )

            position.sell_order = API.submit_order(
                symbol=position.stock.data["symbol"],
                qty=position.qty,
                side="sell",
                type="market",
                time_in_force="day",
            )
