from sourcing_strats.sourcing_strategy_base import SourcingStrategy
from stock import Stock
from requests import get
from bs4 import BeautifulSoup
from util.alpaca_util import is_tradable

NUM_TO_CHECK = 30


class ShortSqueeze(SourcingStrategy):
    def get_stocks(self):
        ret = set()
        results = get("https://apewisdom.io/api/v1.0/filter/all-stocks/page/1").json()[
            "results"
        ][:NUM_TO_CHECK]
        for r in results:
            if not is_tradable(r["ticker"]):
                continue
            ret.add(Stock(r["ticker"]))
        return ret
