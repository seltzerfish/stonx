# from pygooglenews import GoogleNews
# from pprint import pprint
# from util.web_util import get_header, scrape_stock_symbols
# from util.alpaca_util import is_tradable
# from bs4 import BeautifulSoup
# import requests
# from collections import defaultdict
# from sourcing_strats.sourcing_strategy_base import SourcingStrategy
# from stock import Stock

# gn = GoogleNews()


# class GoogNewsBest(SourcingStrategy):
#     def get_stocks(self):
#         return get_goog("stocks to buy")


# def get_goog(query, pages_to_search=7, max_stocks=50):
#     stocks = defaultdict(int)
#     results = gn.search(query, when="2d")["entries"][:pages_to_search]
#     for r in results:
#         print(r["title"])
#         try:
#             soup = BeautifulSoup(
#                 requests.get(r["link"], headers=get_header(), timeout=1).text,
#                 "html.parser",
#             )
#             paragraphs = " ".join([str(tag) for tag in soup.find_all("p")])
#             if not paragraphs:
#                 paragraphs = " ".join([str(tag) for tag in soup.find_all("body")])
#             symbols = scrape_stock_symbols(paragraphs)
#             for s in symbols:
#                 stock = Stock(s)
#                 if (not stock in stocks) and (not is_tradable(s)):
#                     continue
#                 stocks[stock] += 1

#         except requests.exceptions.Timeout:
#             print("request timed out")
#     sorted_dict = sorted(stocks.items(), key=lambda e: e[1], reverse=True)
#     NEWS_STOCKS = [key for key, val in sorted_dict]
#     stocks = set(NEWS_STOCKS[:max_stocks])
#     return stocks
