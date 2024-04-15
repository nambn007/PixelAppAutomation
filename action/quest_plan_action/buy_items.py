import time
import traceback
from selenium.webdriver.support import expected_conditions as EC
from typing import List

import selenium
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

import const
from images import test
from model.driver_control import DriverControl

from model.quest import Quest


def buy_item(self, driverControl: DriverControl, quest: Quest):
    # reset value
    self.is_reload = False
    self.options_item_buy = []
    # ---------------------------

    actions = driverControl.action_chains()
    driver = driverControl.driver
    time.sleep(3)

    # open market
    screen_shot_path = f'{const.CURRENT_PATH_DIRECTORY}/images/hazel_quest/overview_open_market.png'
    driverControl.driver.save_screenshot(screen_shot_path)
    x, y = test.get_position(screen_shot_path,
                             f'{const.CURRENT_PATH_DIRECTORY}/images/hazel_quest/enter_market.png')
    actions.move_by_offset(x, y).click().perform()
    actions.move_by_offset(-x, -y).perform()
    time.sleep(1.5)

    while True:
        counter = 0
        print("zodayy ??")
        # Check xem có hiện danh sách item không. nếu có thì bắt đầu tìm kiếm, time out thì tắt tab đi bật lại
        check_show_item = driver.find_elements(By.CLASS_NAME, 'Marketplace_item__l__LM')
        if len(check_show_item) > 0:
            break
        time.sleep(0.5)
        counter += 1
        if counter >= 10:  # delay 4s k hien reset action
            print("press: ???ESCAPE")
            actions.key_down(Keys.ESCAPE).perform()
            time.sleep(1)
            self.buy_item(driverControl, quest)

    filter_market_item = driver.find_element(By.CLASS_NAME, 'Marketplace_filter__3ynr2')

    # nhập item need buy
    [filter_market_item.send_keys(i) for i in quest.quest_name]
    items = driver.find_elements(By.CLASS_NAME, 'Marketplace_items__Jw4De')
    for item in items:
        print("butaaa_view_lisst")

        button_view_list = self.find_element_2_class('commons_pushbutton__7Tpa3', 'Marketplace_viewListings__q_KfD',
                                                     item).click()
        print("clicked", button_view_list, type(button_view_list))

        name = WebDriverWait(item, 30).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "Marketplace_itemName__Recoz")))
        # nếu tên trên list item trùng với item cần mua
        print(f"name.text >> {name.text} --- item_name >> {quest.quest_name}")
        if name.text == quest.quest_name:
            print("click button_lisst_view")
            button_view_list = self.find_element_2_class('commons_pushbutton__7Tpa3',
                                                         'Marketplace_viewListings__q_KfD', driver)

            try:
                button_view_list.click()
            except Exception as e:
                pass

            all_element_price = self.find_elements_2_class('commons_pushbutton__7Tpa3',
                                                           'MarketplaceItemListings_buyListing__jYwuF', driver)
            print("show lisst buy", type(all_element_price))
            # Duyệt qua tất cả các item có thể mua (nếu nó bị disable thì k lấy )
            for item_elem in all_element_price:
                string_price = item_elem.text
                button_item_buy_status = item_elem.get_attribute('disabled')
                if button_item_buy_status is None:
                    string_price = string_price.replace(" ", "")
                    last_at_index = string_price.rfind("@")
                    if last_at_index == -1:
                        continue
                    last_colon_index = string_price.rfind(":", 0, last_at_index)

                    result = string_price[last_colon_index + 1: last_at_index]
                    print("result1", result)

                    if result == "Allitem":
                        continue
                    print("result2", result)
                    self.options_item_buy.append({"button": item_elem, "quantity": int(result)})
            elemt_max_quantyti_item = max(self.options_item_buy, key=lambda i: i["quantity"])["button"]
            elemt_max_quantyti_item.click()
            print("clicked item with most of price!")
            """Đến đây có các trường hơp:
            - K Đủ tiền:
                 => dừngg
            - Đủ tiền  
                Số lượng mua được không đủ sl quest thuwjc cần
                    > mua lại lần 2 bằng lần trước đó + vào (Tổng 8: lần trc đã mua 3, lần 2 mua 5 )
                        > tạo vòng lặp cho đén khi đủ quest
                Nguoi ban , ban du. nhung 

            """
            total_quantity_item: int = max(self.options_item_buy, key=lambda i: i["quantity"])["quantity"]

            board_buy = driverControl.web_driver_wait('MarketplaceItemListings_content__eeHjR', 'class')

            while True:
                if self.is_reload == True:
                    # Nếu nhảy vào đây nghĩa là từng mua fail và cần reload lại list item để mua lại
                    actions.key_down(Keys.ESCAPE).perform()
                    time.sleep(0.5)
                    self.buy_item(driverControl, quest)
                number_item_bought = 0
                input_price = WebDriverWait(board_buy, 30).until(
                    EC.visibility_of_element_located((By.TAG_NAME, "input"))
                )

                input_price.clear()
                [input_price.send_keys(i) for i in str(quest.quantity)]

                try:
                    button_but_or_not = self.find_elements_2_class("commons_pushbutton__7Tpa3",
                                                                   "MarketplaceItemListings_buyListing__jYwuF",
                                                                   driver)
                except:
                    # Nếu quá lâu không load ra hoặc tìm ra nut mua thì tải lại
                    self.is_reload = True
                    time.sleep(3)
                    continue

                for button in button_but_or_not:
                    print("check button -> buton.ettext", button.text)
                    if 'Buy ' in button.text and 'for ' in button.text:
                        button.click()
                        print("clicked buy!")
                        try:
                            status_content = driverControl.web_driver_wait('Notifications_text__ak1FH',
                                                                           'class')
                            if status_content.text == 'marketplace-purchase-failed':
                                self.is_reload = True
                                time.sleep(3)
                                break
                            else:
                                suscess_inf = WebDriverWait(driver, 30).until(
                                    EC.visibility_of_all_elements_located((By.CLASS_NAME, "Marketplace_prop__fTsfy"))
                                )
                                for elmem in suscess_inf:
                                    time.sleep(1)
                                    print(f"total_in:{elmem.text} ")

                                button = self.find_element_2_class('commons_uikit__Nmsxg', 'commons_pushbutton__7Tpa3',
                                                                   driver)



                        except:
                            continue

                    time.sleep(0.1)
                    if number_item_bought == quest.quantity:
                        break

            time.sleep(30)
            actions.key_down(Keys.ESCAPE).perform()

            break
    print("done??")
    time.sleep(100)
