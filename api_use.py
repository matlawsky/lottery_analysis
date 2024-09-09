"""

data can be easily grabed by API call
https://www.lotto.pl/api/lotteries/draw-results/by-gametype?game=Lotto&index=1&size=7000&sort=drawDate&order=DESC
https://www.lotto.pl/api/lotteries/draw-results/by-gametype?game=EuroJackpot&index=1&size=7000&sort=drawDate&order=DESC
https://www.lotto.pl/api/lotteries/draw-results/by-gametype?game=EkstraPensja&index=1&size=7000&sort=drawDate&order=DESC
https://www.lotto.pl/api/lotteries/draw-results/by-gametype?game=Kaskada&index=1&size=7000&sort=drawDate&order=DESC
https://www.lotto.pl/api/lotteries/draw-results/by-gametype?game=SuperSzansa&index=1&size=5000&sort=drawDate&order=DESC
https://www.lotto.pl/api/lotteries/draw-results/by-gametype?game=MultiMulti&index=1&size=15000&sort=drawDate&order=DESC
https://www.lotto.pl/api/lotteries/draw-results/by-gametype?game=MiniLotto&index=1&size=7000&sort=drawDate&order=DESC

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import json
import time
from random import randint
from bs4 import BeautifulSoup
import re
import pandas as pd

def main():
    # start measuring time
    start_time = time.time()
    t = time.localtime()
    # instantiate a driver
    data_dict = {}
    url = "https://www.lotto.pl/api/lotteries/draw-results/by-gametype?game=MiniLotto&index=1&size=7000&sort=drawDate&order=DESC"
    driver = webdriver.Chrome()
    driver.get(url)

    soup=BeautifulSoup(driver.page_source, 'lxml')
    data = json.loads(soup.text)
    with open(f"minilotto_data_api.json", "w+", encoding="utf-8") as d:
        json.dump(data, d, indent=4)

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
