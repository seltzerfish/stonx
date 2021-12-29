from util.alpaca_util import get_current_price

class Stock:
    def __init__(self, symbol):
        self.data = dict()
        self.data["symbol"] = symbol

    def get_price(self):
        if "price" in self.data:
            return self.data["price"]
        self.data["price"] = get_current_price(self.data["symbol"])
        return self.data["price"]

    def __hash__(self):
        return hash(self.data["symbol"])

    def __eq__(self, other):
        return self.data["symbol"] == other.data["symbol"]

    def __str__(self):
        return self.data["symbol"]

    def __repr__(self):
        return self.data["symbol"]
