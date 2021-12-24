import strategy_list
from trade_bot import TradeBot
from time import sleep
from util import alpaca_util

if __name__ == "__main__":
    alpaca_util.cancel_all_orders()
    alpaca_util.sell_all_positions()
    try:
        trade_bot = TradeBot(strategy_list.TEST_STRATEGY)
        while True:
            if alpaca_util.market_open():
                trade_bot.update()
            else:
                sleep(60)
    except Exception as e:
        print(e)
        alpaca_util.cancel_all_orders()
        alpaca_util.sell_all_positions()
