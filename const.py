import json
from typing import List

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from datetime import datetime

"""DRIVER CHORM THEO TỪNG PROFILE CỦA GEN"""


def chorm_driver(ws_endpoint: str, index: int) -> selenium.webdriver.chrome.webdriver.WebDriver:
    chrome_driver = DRIVER_CHORM_PATH
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", ws_endpoint)
    service = Service(executable_path=chrome_driver)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    x: int = index * WIDTH_WINDOW
    y: int = 10
    driver.set_window_rect(x=x, y=y, width=WIDTH_WINDOW, height=HEIGHT_WINDOW)

    return driver


"""PATH CHORM DRIVER"""
DRIVER_CHORM_PATH: str = R'/allPythonProject/selenium-auto/Selenium-Pixels/chromedriver.exe'

"""CONFIG WINDOW SIZE"""
WIDTH_WINDOW: int = 700
HEIGHT_WINDOW: int = 480

"""TIME OUT STANDRAD"""
TIME_OUT_FINDING_ELEMENT: int = 30  # (second)

"""CURRENT_TIME"""
CURRENT_TIME_NOW: str = datetime.now().strftime('%Y%m%d-%H%M%S')

"""CURRENT_PATH"""
CURRENT_PATH_DIRECTORY: str = r'D:/allPythonProject/selenium-auto/Selenium-Pixels'

"""REQUEST PRICE ITEM"""
ID_USER_REQUEST: str = '65f5dd9fca1af871f13456ea'
def get_id_item(itemName: str) -> str:
    with open(r'D:\allPythonProject\selenium-auto\Selenium-Pixels\itemConfig.json', 'r') as file:
        return json.load(file).get(itemName)

"""SPECIAL ITEM"""
LIST_SPECIAL_ITEMS:List[str] = ['Java Bean']

