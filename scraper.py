"""

This parser is only demonstration, this data can be easily grabed by API call
https://www.lotto.pl/api/lotteries/draw-results/by-gametype?game=Lotto&index=1&size=7000&sort=drawDate&order=DESC

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

url = "https://www.lotto.pl/lotto/wyniki-i-wygrane/number,"


# return text of the element or error messafe
def try_find_element(driver, xpath, not_found_message):
    # find single element using it's xpath
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element = driver.find_element(By.XPATH, xpath).text
        return element
    except NoSuchElementException:
        return not_found_message
    except:
        return f"Unknown exception at {xpath}"


# every new draw only single row needs to be checked
def get_single_draw_data(driver, input_dict, n):
    driver.get(f"{url}{n}")
    # handling accept button
    try:
        driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[2]/div/div[4]/div[2]/div[3]/div/button",
        ).click()
    except:
        pass
    element = try_find_element(
        driver,
        '//div[contains(@class,"game-main-box skip-contrast")]',
        "error",
    )
    input_dict.update({n: element})
    return input_dict


# loop through alterneting urls from starting number to ending number
def get_draws_data(driver, start, end):
    elements = []
    elements_dict = {}
    for i in range(start, end):
        driver.get(f"{url}{i}")
        # add random delay after call to simulate user interaction
        delay = randint(5, 15)
        time.sleep(delay / 10)
        # handling the accept button
        try:
            driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div/div/div[2]/div/div[4]/div[2]/div[3]/div/button",
            ).click()
        except:
            pass
        element = try_find_element(
            driver,
            '//div[contains(@class,"game-main-box skip-contrast")]',
            "error",
        )
        elements.append(element)

    n = 0
    for elem in elements:
        n = n + 1
        elements_dict.update({n: elem})
    return elements_dict


def main():
    # start measuring time
    start_time = time.time()
    t = time.localtime()
    # instantiate a driver
    data_dict = {}
    driver = webdriver.Chrome()
    with open(f"lotto_data.json", "r+", encoding="utf-8") as d:
        data_dict = json.load(d)
    dict_data = get_single_draw_data(driver, data_dict, 6856)
    # elements_dict = gather_all_data(driver,1, 6856)

    with open(f"lotto_data.json", "w+", encoding="utf-8") as d:
        json.dump(dict_data, d, indent=4)

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
