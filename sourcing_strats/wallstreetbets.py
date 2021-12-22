from sourcing_strats.sourcing_strategy_base import SourcingStrategy
import requests
from util.web_util import get_header, scrape_stock_symbols
from util.alpaca_util import is_tradable
from bs4 import BeautifulSoup
from stock import Stock

WSB_URL = "https://www.reddit.com/r/wallstreetbets/"
WSB_YOLO_URL = "https://www.reddit.com/r/wallstreetbets/search?sort=top&q=flair%3AYOLO&restrict_sr=on&t=day"


class WSBHot(SourcingStrategy):
    def get_stocks(self):
        symbols = set()
        soup = BeautifulSoup(
            requests.get(WSB_URL, headers=get_header(), timeout=10).text,
            "html.parser",
        )
        for node in soup.find_all("a"):
            content = scrape_stock_symbols(node.find(text=True))
            if content and is_tradable(content[0]):
                stock = Stock(content[0])
                symbols.add(stock)
        return symbols
