import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

pytest.fixture()
def setup(browser):
    if browser.lower() or browser.upper() == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        print("Chrome driver launched successfully")
        time.sleep(5)

    elif browser.lower() or browser.upper() == 'firefox':
        driver = webdriver.Firefox()
        print("Firefox driver launched successfully")
    else:
        driver = webdriver.Edge()
        print("Edge driver launched successfully")

    return driver


set("none")

print("print someting")
