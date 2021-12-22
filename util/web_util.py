from random import choice
import re


def get_header():
    headers = {"user-agent": _get_random_ua(), "referer": "https://google.com"}
    return headers


def _get_random_ua():
    with open("/Users/connerlane/git/stonx/util/ua.txt", "r") as f:
        ua_list = [line.strip() for line in f]
        return choice(ua_list)


def scrape_stock_symbols(text):
    try:
        results = re.findall(r"[A-Z]{2,4}", text)
        return results
    except:
        return []
