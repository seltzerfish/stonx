# STONX BABY

## First time setup


1. pip install requirements.txt in a new `venv`.
2. Make a `creds.py` file, and create a `dict` literal called `PAPER`, and include your alpaca keys like this:

```
PAPER = {
    "endpoint": "https://paper-api.alpaca.markets",
    "api_key": "ABCDEFGHIJKLMOP",
    "secret_key": "ABCDEFGHIJKLMOP",
}
```

## Regular Usage
This is a modular framework that aims to abstract and separate the higher level strategy while automating the tedious low-level work. You need only provide 3 things:
1. Your **sourcing** strategy - *Where* to look for stocks.
2. Your **buying** strategy - *How* to pick which stock(s) to buy.
3. your **selling** strategy - *When* to sell.

Create your 3 strategies in the appropriate subpackages (or use existing ones). Once you've got your 3 strategies, you can put them together into a single `Strategy` object in `strategy_list.py`.

Lastly, in `main.py`, change out the name of the strategy being used for the one you created, and run `main.py`.