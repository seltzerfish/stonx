import alpaca_trade_api as alpaca
from creds import PAPER, REAL

MAX_POSITIONS = 5  # TODO: put this in Strategy?
USING_REAL_MONEY = False
MIN_STOCK_PRICE = 10

if USING_REAL_MONEY:
    API = alpaca.REST(REAL["api_key"], REAL["secret_key"], REAL["endpoint"])
else:
    API = alpaca.REST(PAPER["api_key"], PAPER["secret_key"], PAPER["endpoint"])
