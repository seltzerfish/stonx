from sourcing_strats.sourcing_strategy_base import SourcingStrategy
from stock import Stock
from util.alpaca_util import is_tradable
from selenium import webdriver
from time import sleep
from creds import LEVELFIELDS
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class LatestBullish(SourcingStrategy):
    def get_stocks(self):
        print("getting latest bullish")
        stocks = set()
        driver = webdriver.Firefox()
        driver.get("https://app.levelfields.ai/dashboard")
        elem = driver.find_element(By.NAME, "email")
        elem.clear()
        elem.send_keys(LEVELFIELDS["email"])
        elem = driver.find_element(By.NAME, "password")
        elem.clear()
        elem.send_keys(LEVELFIELDS["password"])
        elem.send_keys(Keys.RETURN)
        sleep(5)
        driver.get("https://app.levelfields.ai/dashboard")
        sleep(5)
        table = driver.find_element(By.CLASS_NAME, "Table")
        rows = table.find_elements(By.CLASS_NAME, "Table-row")[1:]
        for r in rows:
            try:
                ticker = r.find_element(By.CLASS_NAME, "TableRow-company-symbol").text
                scenario = r.find_element(By.CLASS_NAME, "TableScenarioName").text
                bullish = "bull" in r.find_element(
                    By.CLASS_NAME, "t-center"
                ).find_element(By.TAG_NAME, "img").get_attribute("src")
                if bullish and is_tradable(ticker):
                    s = Stock(ticker)
                    s.data["scenario"] = scenario
                    stocks.add(s)
            except Exception as e:
                # print(e)
                break
        driver.close()
        return stocks
