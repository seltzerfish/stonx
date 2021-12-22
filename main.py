import strategy_list
from trade_bot import TradeBot
from time import sleep
from util import alpaca_util

if __name__ == "__main__":
    trade_bot = TradeBot(strategy_list.BASIC_STRATEGY)
    while True:
        if alpaca_util.market_open():
            trade_bot.update()
        else:
            sleep(60)
