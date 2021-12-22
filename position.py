from constants import API
from time import sleep


class Position:
    def __init__(self, stock, buy_order, sell_strategy):
        self.stock = stock
        self.buy_order = buy_order
        self.sell_order = None
        self.exited = False
        self.sell_strategy = sell_strategy
        self.entry_price = 0
        self.qty = 0
        self.investment = 0
        self.wait_for_buy_order_to_fill()

    def wait_for_buy_order_to_fill(self):
        placed_buy_order = API.get_order(self.buy_order.id)
        while not placed_buy_order.filled_qty == placed_buy_order.qty:
            sleep(0.1)
            placed_buy_order = API.get_order(self.buy_order.id)
        self.qty = placed_buy_order.filled_qty
        self.entry_price = float(placed_buy_order.filled_avg_price)
        self.investment = self.entry_price * float(placed_buy_order.qty)

    def update(self):
        self.sell_strategy.update(self)
        if not self.sell_order:
            return
        placed_sell_order = API.get_order(self.sell_order.id)
        if placed_sell_order and placed_sell_order.filled_at:
            self.exit()

    def buy_order_filled(self):
        pass

    def has_been_sold(self):
        if not self.sell_order:
            return False
        placed_sell_order = API.get_order(self.sell_order.id)
        if placed_sell_order and placed_sell_order.filled_at:
            return True
        return False

    def exit(self):
        self.exited = True
        print("{} has been sold.".format(self.stock.data["symbol"]))
