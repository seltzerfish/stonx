from sourcing_strats.sourcing_strategy_base import SourcingStrategy
import requests
from util.web_util import get_header, scrape_stock_symbols
from util.alpaca_util import is_tradable
from bs4 import BeautifulSoup
from stock import Stock

GAINERS_URL = "https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/"
LOSERS_URL = "https://www.tradingview.com/markets/stocks-usa/market-movers-losers/"
VOLATILE_URL = (
    "https://www.tradingview.com/markets/stocks-usa/market-movers-most-volatile/"
)
ACTIVE_URL = "https://www.tradingview.com/markets/stocks-usa/market-movers-active/"
OVERBOUGHT_URL = (
    "https://www.tradingview.com/markets/stocks-usa/market-movers-overbought/"
)


class TopMovers(SourcingStrategy):
    def get_stocks(self):
        return pull_trading_view(GAINERS_URL, "TV_TOP_GAINERS")


class TopLosers(SourcingStrategy):
    def get_stocks(self):
        return pull_trading_view(LOSERS_URL, "TV_TOP_LOSERS")


class MostVolatile(SourcingStrategy):
    def get_stocks(self):
        return pull_trading_view(VOLATILE_URL, "TV_VOLATILE")


class MostActive(SourcingStrategy):
    def get_stocks(self):
        return pull_trading_view(ACTIVE_URL, "TV_MOST_ACTIVE")


class Overbought(SourcingStrategy):
    def get_stocks(self):
        return pull_trading_view(OVERBOUGHT_URL, "TV_OVERBOUGHT")


def pull_trading_view(url, source):
    try:
        symbols = set()
        soup = BeautifulSoup(
            requests.get(url, headers=get_header(), timeout=10).text,
            "html.parser",
        )
        for node in soup.find_all("a", {"class": "tv-screener__symbol"}):
            content = scrape_stock_symbols(node.find(text=True))
            if content and is_tradable(content[0]):
                stock = Stock(content[0])
                # stock.data["source"] = source
                symbols.add(stock)
        return symbols
    except Exception as e:
        print(e)
        print("request to tradingview.com timed out")
        return set()
