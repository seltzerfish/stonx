from abc import abstractmethod, ABC
from constants import API


class BuyingStrategy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def choose_stock_to_buy(self, stocks):
        pass

    def prepare(self):
        # Does nothing by default.
        # If you need to train a ML model, do it in this method.
        pass

    def buy(self, stock, qty):
        # Default buy() is an immediate market order.
        # Override in child class if desired.
        return API.submit_order(
            symbol=stock.data["symbol"],
            qty=qty,
            side="buy",
            type="market",
            time_in_force="day",
        )
        # stocks_need::to make;money$$
        # peeb
        # <3__!
