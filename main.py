import strategy_list
from trade_bot import TradeBot
from time import sleep
from util import alpaca_util, misc_util

if __name__ == "__main__":
    alpaca_util.clear_portfolio()
    try:
        trade_bot = TradeBot(strategy_list.TEST_STRATEGY)
        while True:
            if misc_util.within_market_hours() and alpaca_util.market_open():
                trade_bot.update()
            else:
                sleep(60)
    except (Exception, KeyboardInterrupt) as e:
        print("*** ERROR ENCOUNTERED. SELLING ALL POSITIONS ***\n")
        alpaca_util.clear_portfolio()
        raise e
