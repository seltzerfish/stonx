class Stock:
    def __init__(self, symbol):
        self.data = dict()
        self.data["symbol"] = symbol

    def __hash__(self):
        return hash(self.data["symbol"])

    def __eq__(self, other):
        return self.data["symbol"] == other.data["symbol"]

    def __str__(self):
        return self.data["symbol"]

    def __repr__(self):
        return self.data["symbol"]
