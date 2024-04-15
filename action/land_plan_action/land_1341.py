import time
from selenium.webdriver import Keys
import const
from model.driver_control import DriverControl
from selenium.webdriver.common.action_chains import ActionChains
from action.js_action import click_position
from action import common_action
from images import test
from action.land_plan_action import land_1342



def claim(driverControl: DriverControl, land_number: int, is_reset_position:bool):
    actions = driverControl.action_chains()

    # reset position user
    if not is_reset_position:
        common_action.reset_land_position(driverControl)
    time.sleep(4)
    # start action


    """if u want skip this land
    """
    actions.key_down(Keys.ARROW_RIGHT).pause(4).key_up(Keys.ARROW_RIGHT).perform()#mid land

    """"""

    # actions.key_down(Keys.ARROW_RIGHT).pause(1).key_up(Keys.ARROW_RIGHT).perform()#mid land
    # time.sleep(0.3)
    #
    # actions.key_down(Keys.ARROW_UP).pause(3.2).key_up(Keys.ARROW_UP).perform()
    # time.sleep(0.3)
    #
    # ##claim egg
    # screen_shot_path = f'images/screen_shot/overview_{driverControl.profile_id}.png'
    # driverControl.driver.save_screenshot(screen_shot_path)
    # x, y = test.get_position(screen_shot_path,f'images/lands/{land_number}/egg_{land_number}.png')
    # actions.move_by_offset(x, y).click().perform()
    # actions.move_by_offset(-x, -y).click().perform()
    # time.sleep(0.5)
    #
    # actions.key_down(Keys.ARROW_LEFT).pause(2.7).key_up(Keys.ARROW_LEFT).perform()  # mid land
    # time.sleep(0.3)
    # screen_shot_path = f'images/screen_shot/overview_{driverControl.profile_id}.png'
    # driverControl.driver.save_screenshot(screen_shot_path)
    #
    # ## clain drill
    # for i in range(1,4):
    #     x_drill, y_drill = test.get_position(screen_shot_path, f'images/lands/{land_number}/drill_{i}_{land_number}.png')
    #     print(f"click dril {i}")
    #     actions.move_by_offset(x_drill, y_drill).click().perform()
    #     time.sleep(0.3)
    #     actions.move_by_offset(0 - x_drill, 0 - y_drill).perform()
    #     time.sleep(0.1)
    #     actions.move_by_offset(x_drill, y_drill).click().perform()
    #     time.sleep(0.3)
    #     actions.move_by_offset(0 - x_drill, 0 - y_drill).perform()
    #     time.sleep(0.1)
    # time.sleep(0.3)
    #
    # actions.key_down(Keys.ARROW_RIGHT).pause(2.7).key_up(Keys.ARROW_RIGHT).perform()
    # time.sleep(0.3)
    #
    # # reset position
    # actions.key_down(Keys.ARROW_DOWN).pause(3.1).key_up(Keys.ARROW_DOWN).perform()
    # time.sleep(0.3)
    # actions.key_down(Keys.ARROW_RIGHT).pause(2.5).key_up(Keys.ARROW_RIGHT).perform()
    if common_action.is_show_display(driverControl):
        land_1342.claim(driverControl, land_number + 1, True)
        return True




