from buying_strats.buying_strategy_base import BuyingStrategy
from random import choice
from lxml import html
from requests import get


class Reddit(BuyingStrategy):
    def choose_stock_to_buy(self, stocks):
        for s in stocks:
            if not "reddit_sentiment" in s.data:
                s.data["reddit_sentiment"] = get_sentiment(s.data["symbol"])
        stocks.sort(key=lambda x: x.data["reddit_sentiment"])
        print(
            stocks[-1].data["symbol"] + " - " + str(stocks[-1].data["reddit_sentiment"])
        )
        return stocks[-1]


def get_sentiment(symbol):
    try:
        return int(
            html.fromstring(get("https://apewisdom.io/stocks/" + symbol).content)
            .xpath("/html/body/div[1]/div[3]/div[2]/div[2]/div/div[1]")[0]
            .text_content()
            .strip()[:-1]
        )
    except:
        return 0
