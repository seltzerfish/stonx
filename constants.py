import alpaca_trade_api as alpaca
from creds import PAPER

API = alpaca.REST(PAPER["api_key"], PAPER["secret_key"], PAPER["endpoint"])
