from position import Position


class Strategy:
    def __init__(self, codename, sourcing_strats, buy_strat, sell_strat):
        self.codename = codename
        self.sourcing_strats = sourcing_strats
        self.buy_strat = buy_strat
        self.sell_strat = sell_strat

    def source(self):
        stocks = set()
        for strat in self.sourcing_strats:
            stocks = stocks.union(strat.source())
        return stocks

    def buy(self, stock, qty):
        print("Placing order to buy {} shares of {}".format(qty, stock.data["symbol"]))
        buy_order = self.buy_strat.buy(stock, qty)
        return Position(stock, buy_order, self.sell_strat)

    def choose_stock(self, stocks):
        return self.buy_strat.choose_stock_to_buy(list(stocks))

    def prepare(self):
        print("Preparing strategy...")
        for strat in self.sourcing_strats:
            strat.prepare()
        self.buy_strat.prepare()
        self.sell_strat.prepare()
        print("Done.")
