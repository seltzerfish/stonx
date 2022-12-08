from constants import API


def is_tradable(symbol):
    if symbol in BLACKLIST or symbol in NON_TRADABLE_CACHE:
        return False
    if symbol in TRADABLE_CACHE:
        return True
    try:
        asset = API.get_asset(symbol)
        if asset.tradable:
            if not symbol in TRADABLE_CACHE:
                TRADABLE_CACHE.add(symbol)
                save_tradable_cache()
            return True
    except:
        pass
    if not symbol in NON_TRADABLE_CACHE:
        NON_TRADABLE_CACHE.add(symbol)
        save_non_tradable_cache()
    return False


def load_blacklist():
    cache = set()
    with open("BLACKLIST.txt", "r") as f:
        [cache.add(line.strip()) for line in f]
    return cache


def load_tradable_cache():
    cache = set()
    with open("cache/tradable_cache.txt", "r") as f:
        [cache.add(line.strip()) for line in f]
    return cache


def load_non_tradable_cache():
    cache = set()
    with open("cache/non_tradable_cache.txt", "r") as f:
        [cache.add(line.strip()) for line in f]
    return cache


def save_tradable_cache():
    with open("cache/tradable_cache.txt", "w") as f:
        tradable = sorted(list(TRADABLE_CACHE))
        for entry in tradable:
            f.writelines(entry + "\n")


def save_non_tradable_cache():
    with open("cache/non_tradable_cache.txt", "w") as f:
        non_tradable = sorted(list(NON_TRADABLE_CACHE))
        for entry in non_tradable:
            f.writelines(entry + "\n")


def market_open():
    CLOCK = API.get_clock()
    return CLOCK.is_open


def get_current_price(stock):
    return API.get_latest_trade(stock.data["symbol"]).price


def sell_all_positions():
    portfolio = API.list_positions()
    for position in portfolio:
        API.submit_order(
            symbol=position.symbol,
            qty=position.qty,
            side="sell",
            type="market",
            time_in_force="gtc",
        )


def cancel_all_orders():
    API.cancel_all_orders()


def clear_portfolio():
    cancel_all_orders()
    sell_all_positions()


BLACKLIST = load_blacklist()
NON_TRADABLE_CACHE = load_non_tradable_cache()
TRADABLE_CACHE = load_tradable_cache()
