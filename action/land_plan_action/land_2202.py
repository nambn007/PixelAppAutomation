from model.driver_control import DriverControl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from action.js_action import click_position
from images import test


def claim(driverControl: DriverControl):
    pass
    # actions = ActionChains(driverControl.driver)
    # print("press -> key")
    # actions.key_down(Keys.ARROW_UP).pause(3).key_up(Keys.ARROW_UP).perform()
    # # time.sleep(0.3)
    # # actions.key_down(Keys.ARROW_RIGHT).pause(2).key_up(Keys.ARROW_RIGHT).perform()
    #
    # print("take screen")
    #
    # driverControl.driver.save_screenshot('images/overview.png')
    #
    # locations = test.get_position("images/overview.png")
    # canvas = driverControl.web_driver_wait('canvas','tag_name')
    #
    #
    #
    # for locate in locations:
    #     x = locate[0]
    #     y = locate[1]
    #     print("click at ", x, y)
    #     #
    #     # x = 335
    #     # y = 35
    #     # driverControl.driver.execute_script(
    #     #     "var evt = new MouseEvent('click', {'view': window, 'bubbles': true, 'cancelable': true, 'clientX': "+str(x)+", 'clientY': "+str(y)+" }); arguments[0].dispatchEvent(evt);",
    #     #     canvas)
    #     # action = ActionChains(driverControl.driver)
    #     # action.move_by_offset(x,y).click().perform()
    #     # time.sleep(2)
    #
    #     click_position.js_click(driverControl, x,y)
    #
    #     # print("click at ", x, y)
    #
    #
    # print("nha")
    # # click_position.js_click(driverControl,14,535)
    #
    #
    #
