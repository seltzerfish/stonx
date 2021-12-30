from math import floor
from util import alpaca_util
from time import sleep
from util.misc_util import market_closing_soon


class TradeBot:
    def __init__(self, strategy, equity=10000, max_positions=4):
        self.positions = []
        self.strategy = strategy
        self.equity = equity
        self.max_positions = max_positions
        self.strategy.prepare()

    def update(self):
        self.update_positions()
        sleep(3)  # some buffer time to prevent the API from ratelimiting us
        if self.should_buy():
            self.buy()

    def update_positions(self):
        for p in self.positions:
            p.update()
        self.remove_exited_positions()

    def remove_exited_positions(self):
        self.positions = [p for p in self.positions if not p.exited]

    def should_buy(self):
        if market_closing_soon():
            return False
        if len(self.positions) < self.max_positions:
            return True
        return False

    def buy(self):
        # source list of stocks
        stocks = self.strategy.source()
        self.remove_stocks_already_holding(stocks)
        # pick one from the list
        stock_to_buy = self.strategy.choose_stock(stocks)
        # buy it
        position = self.strategy.buy(stock_to_buy, self.calculate_qty(stock_to_buy))
        self.positions.append(position)

    def remove_stocks_already_holding(self, stocks):
        for p in self.positions:
            stocks.remove(p.stock)

    def calculate_qty(self, stock):
        price = stock.get_price()
        return floor((self.equity / self.max_positions) / price)
