import time
from source.source_genloin.gen_connect import GenloginAction
from source.source_genloin.gen_connect import GenloginConnection
from action import login
from action import common_action
from action.quest_plan_action.finish_quest import QuestReturn
import selenium
from model.driver_control import DriverControl
from action.land_plan_action import land_2202, land_1340, land_1341


def action(driver: selenium.webdriver.chrome.webdriver.WebDriver, profile_id: int) -> None:
    try:
        driverControl = DriverControl(driver, profile_id)
        signal_login = login.login_pixels(driverControl)

        if signal_login:
            pass
            # #RUNNING-LAND ----------------------------
            # print("book_mark")
            # land_number: int = 1340
            # signal_tele = common_action.select_land_book_mark(driverControl, land_number)
            # if signal_tele and common_action.is_show_display(driverControl):
            # #         if common_action.is_show_display(driverControl):
            #     is_done_1340 = land_1340.claim(driverControl, land_number, False)
            # # ----------------------------

            #QUEST AUTOMATION
            QuestReturn().finish_quest(driverControl)




        GenloginAction().stop_profile(profile_id)

    except Exception as e:
        print(f"Exception > action_thread.py > action :{e}")
        [GenloginAction().stop_profile(id) for id in GenloginConnection().get_id_profile_running()]
