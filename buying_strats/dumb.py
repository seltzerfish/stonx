from buying_strats.buying_strategy_base import BuyingStrategy
from random import choice


class RandomBuy(BuyingStrategy):
    def choose_stock_to_buy(self, stocks):
        return choice(stocks)
