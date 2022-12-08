from sourcing_strats.sourcing_strategy_base import SourcingStrategy
from stock import Stock
from util.alpaca_util import is_tradable


class Hardcoded(SourcingStrategy):
    def get_stocks(self):
        return set(
            [
                Stock(s)
                for s in [
                    "UHT",
                    "LZB",
                    "COFS",
                    "DASH",
                    "GWRS",
                    "ENB",
                    "STER",
                ]
                if is_tradable(s)
            ]
        )
