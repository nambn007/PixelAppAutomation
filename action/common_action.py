import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

from model.driver_control import DriverControl


def is_show_display(driverContorl: DriverControl):
    try:
        time.sleep(2)
        check_in_game = driverContorl.invisibility_of_element(
            '//*[@id="__next"]/div/div[3]/div/div[1]/div/div[1]/div/div[2]/div/img', 'xpath')
        if check_in_game:
            print("display : true")
            return True
    except:
        print("display : false")
        is_show_display(driverContorl)
def select_land_book_mark(driverControl: DriverControl, land_number: str):
    print("select_land_book_mark: selecting...")
    time.sleep(2)
    click_select_land = driverControl.web_driver_wait(
        '//*[@id="__next"]/div/div[3]/div/div[1]/div/div[1]/div/button[1]', 'xpath')
    click_select_land.click()

    button_bookmark = driverControl.web_driver_wait('//*[@id="__next"]/div/div[3]/div/div[3]/div[4]/button[3]', 'xpath')
    button_bookmark.click()

    # finding land

    list_land = driverControl.web_driver_wait('//*[@id="__next"]/div/div[3]/div/div[3]/div[5]/div[2]', 'xpath')

    lands = list_land.find_elements(By.CLASS_NAME, 'LandAndTravel_mapSquare__LuVEh')
    for land in lands:
        print(f"-{repr(land.text)}-")
        text_element = land.text.split('\n')
        land_number_element = text_element[0]
        if land_number_element == f'#{land_number}':
            button_tele = land.find_element(By.CLASS_NAME, 'LandAndTravel_buttonTeleport__Z6fS4')
            button_tele.click()
            print(f"button tele to land #{land_number} was clicked! ")
            time.sleep(5)
            return True

    return False
def reset_land_position(driverControl: DriverControl):
    driverControl.action_chains().key_down(Keys.ARROW_DOWN).pause(0.15).key_up(Keys.ARROW_DOWN).perform()
    time.sleep(1)
    driverControl.action_chains().key_down(Keys.ARROW_LEFT).pause(3).key_up(Keys.ARROW_LEFT).perform()
    time.sleep(2)
    is_show = is_show_display(driverControl)
    if is_show:
        time.sleep(3)
        driverControl.action_chains().key_down(Keys.ARROW_RIGHT).pause(2).key_up(Keys.ARROW_RIGHT).perform()
        while True:
            time.sleep(0.5)
            if is_show_display(driverControl):
                return
