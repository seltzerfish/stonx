import strategy_list
from trade_bot import TradeBot
from time import sleep
from util import alpaca_util
from datetime import datetime

if __name__ == "__main__":
    alpaca_util.clear_portfolio()
    try:
        trade_bot = TradeBot(strategy_list.GOOG_NEWS_TEST_STRATEGY)
        while True:
            if alpaca_util.market_open():
                trade_bot.update()
            else:
                print(
                    "market closed. sleeping 60s. current time: {}".format(
                        datetime.now()
                    )
                )
                sleep(60)
    except (Exception, KeyboardInterrupt) as e:
        print("error encountered. clearing portfolio.")
        alpaca_util.clear_portfolio()
        raise e
