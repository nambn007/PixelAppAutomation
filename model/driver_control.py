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


class DriverControl:
    def __init__(self, driver: selenium.webdriver.chrome.webdriver.WebDriver, profile_id: int):
        self.driver = driver
        self.profile_id = profile_id


    def action_chains(self):
        return ActionChains(self.driver)


    def web_driver_wait(self, pamrams_find: str, type_find: str):
        try:
            time.sleep(1)
            if type_find == "id":
                return WebDriverWait(self.driver, const.TIME_OUT_FINDING_ELEMENT).until(
                    EC.presence_of_element_located((By.ID, pamrams_find))
                )
            elif type_find == "xpath":
                return WebDriverWait(self.driver, const.TIME_OUT_FINDING_ELEMENT).until(
                    EC.presence_of_element_located((By.XPATH, pamrams_find))
                )
            elif type_find == "css":
                return WebDriverWait(self.driver, const.TIME_OUT_FINDING_ELEMENT).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, pamrams_find))
                )
            elif type_find == "class":
                return WebDriverWait(self.driver, const.TIME_OUT_FINDING_ELEMENT).until(
                    EC.presence_of_element_located((By.CLASS_NAME, pamrams_find))
                )
            elif type_find == "tag_name":
                return WebDriverWait(self.driver, const.TIME_OUT_FINDING_ELEMENT).until(
                    EC.presence_of_element_located((By.TAG_NAME, pamrams_find))
                )
        except NoSuchElementException:
            # Handle the specific exception raised (e.g., element not found)
            print("model - driver_control: Element not found. Handling the exception.")

        except Exception as e:
            # Handle any other unexpected exceptions
            print("model - driver_control: An unexpected exception occurred:", str(e))

    def invisibility_of_element(self, pamrams_find, type_find):
        try:
            time.sleep(1)
            if type_find == "id":
                check = WebDriverWait(self.driver, const.TIME_OUT_FINDING_ELEMENT).until(EC.presence_of_element_located(
                    (By.ID, pamrams_find)))
                return True
            elif type_find == "xpath":
                check = WebDriverWait(self.driver, const.TIME_OUT_FINDING_ELEMENT).until(EC.presence_of_element_located(
                    (By.XPATH, pamrams_find)))
                return True
            elif type_find == "css":
                check = WebDriverWait(self.driver, const.TIME_OUT_FINDING_ELEMENT).until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, pamrams_find)))
                return True
            elif type_find == "class":
                 check = WebDriverWait(self.driver, const.TIME_OUT_FINDING_ELEMENT).until(EC.presence_of_element_located(
                    (By.CLASS_NAME, pamrams_find)))
                 return True
            elif type_find == "tag_name":
                 check = WebDriverWait(self.driver, const.TIME_OUT_FINDING_ELEMENT).until(EC.presence_of_element_located(
                    (By.TAG_NAME, pamrams_find)))
                 return True
        except NoSuchElementException:
            # Handle the specific exception raised (e.g., element not found)
            print("model - driver_control: Element not found. Handling the exception.")

        except Exception as e:
            # Handle any other unexpected exceptions
            print("model - driver_control: An unexpected exception occurred:", str(e))
