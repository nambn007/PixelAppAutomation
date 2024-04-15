import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from model.driver_control import DriverControl


def login_pixels(driverControl: DriverControl):
    driver = driverControl.driver

    driver.get("https://play.pixels.xyz")
    # driver.get("file:///D:/allPytho/nProject/selenium-auto/Selenium-Pixels/test_position_click.html")
    time.sleep(2)

    choose_server = driverControl.web_driver_wait( pamrams_find='//*[@id="__next"]/div/div[3]/div[2]/div[2]',
                                                   type_find='xpath')
    choose_server.click()
    time.sleep(2)
    server_number = driverControl.web_driver_wait( pamrams_find='//*[@id="__next"]/div/div[3]/div[2]/div[3]/div[89]/button/div',
                                                   type_find='xpath')
    server_number.click()
    time.sleep(3)

    try:
        time.sleep(5)
        #
        check_in_game = driverControl.invisibility_of_element('//*[@id="__next"]/div/div[3]/div/div[1]/div/div[1]/div/div[2]/div/img','xpath')
        # check_in_game = True
        if check_in_game:
            print("okela trueee")
            return True
        else:
            driver.refresh()
            login_pixels(driverControl)
    except Exception as e:
        driver.refresh()
        login_pixels(driverControl)
        return False
