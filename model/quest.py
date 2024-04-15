import time
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import const
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Quest:
    def __init__(self, quest_name: str,
                 quantity: int,
                 button_element: WebElement = None,
                 is_disable: str = None):
        self.quest_name = quest_name
        self.quantity = quantity
        self.button_element = button_element
        self.is_disable = is_disable

    def total_price(self) -> float:
        """
        Lấy ra giá trị hiện tại của quest đó
        """
        curent_price_item = 10 #get from api
        return self.quantity*curent_price_item
