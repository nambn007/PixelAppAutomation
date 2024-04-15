import time
import traceback
from selenium.webdriver.support import expected_conditions as EC
from typing import List

import selenium
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from service import get_price_item
import const
from images import test
from model.driver_control import DriverControl

from model.quest import Quest


class QuestReturn:
    def __init__(self):
        self.counter_refresh = 0
        self.list_info = []
        self.options_item_buy = []
        self.bought_price = 0
        self.quantity_bought = 0
        self.is_reload = False #refresh action
        self.is_stop = False #stop action

    def finish_quest(self, driverControl: DriverControl):
        try:
            is_open_list = self.open_hazel_shop(driverControl)
            if True:
                if is_open_list:
                    button_orders = driverControl.web_driver_wait(
                        '//*[@id="__next"]/div/div[4]/div/div[1]/div[2]/div/div[2]/div[2]/button[2]', "xpath")
                    button_orders.click()
                    time.sleep(1)

                quest_boxes = driverControl.driver.find_elements(By.CLASS_NAME, 'Store_card-content__WhHqh')

                while True:
                    self.list_info = self.all_quest_show(quest_boxes)
                    if len(self.list_info) > 0:
                        time.sleep(0.2)
                        # click close hazel quest board
                        driverControl.web_driver_wait('commons_closeBtn__UobaL', 'class').click()

                        # delete element button, which help find image and click to open market
                        trad_quest = driverControl.web_driver_wait('Hud_topRightBackground__z4cEZ', 'class')
                        driverControl.driver.execute_script(
                            "arguments[0].style.width='10px'; arguments[0].style.height='10px';", trad_quest)
                        # 0-------------------------------------------------------------------------------

                        time.sleep(1)
                        break
                    else:
                        print("Error")
                        # if self.counter_refresh == 30:
                        time.sleep(0.5)
                        continue

                # Di chuyển lấy đồ
                driverControl.action_chains().key_down(Keys.ARROW_UP).pause(4).key_up(Keys.ARROW_UP).perform()

                for index, quest in enumerate(self.list_info):
                    self.buy_item(driverControl, quest)
                # self.buy_item(driverControl, 'Grainbow')

        except Exception as e:
            print(f"EXCEPTION: action > finish_quest > :{e}")

            traceback.print_exc()

    def all_quest_show(self, quest_boxes: selenium.webdriver.remote.webelement.WebElement) -> List[Quest]:
        from common import common_variables
        """
        :param quest_boxes: Element Quest Box
        :return: Trả về danh sách quest có thể mua (sau khi tính toán tổng giá trị mua của quest đó ở mức quy định)
        """
        quests = []
        for box in quest_boxes:
            try:
                quantity = box.find_element(By.CLASS_NAME, 'Store_item-quantity__cFhDE')
                number_reward = box.find_element(By.CLASS_NAME, 'commons_balanceDisplay__NSs8e')
                quest_name = box.find_element(By.CLASS_NAME, 'Store_card-title__InPpB')
                button = self.find_element_2_class('Store_btn-max__Vxg7c', 'commons_pushbutton__7Tpa3', box)
                button_status = button.get_attribute('disabled')
                print("dddd:",number_reward.text,repr(button_status))

                # if quest_name not in ''
                if quest_name in const.LIST_SPECIAL_ITEMS and button_status == 'None':
                    #nếu quest name là các mặt hàng không thể mua bán trên chợ thì check xem có trong tui k,
                    #nếu có thì trả luôn, còn không thì thôi
                    try:
                        button.click()#Tra quest
                    except:
                        pass
                    continue

                elif int(number_reward.text) == 1 or int(number_reward.text) == 5:
                    #Nếu Quest là Pixels
                    total_value_pixel_item = int(quantity.text[1:]) *get_price_item.get_price(id_item=const.get_id_item(quest_name),
                                                                      pid=const.ID_USER_REQUEST)
                    #nếu vượt quá "total_value_pixel_item" thì k lay
                    if total_value_pixel_item <= common_variables.TOTAL_LIMIT_PIXEL_QUEST:
                        print(f"total $Pixel quest: {quest_name} - {total_value_pixel_item}")
                        try:
                            button.click()#Tra quest
                        except:
                            pass
                        quests.append(
                            Quest(quantity=int(quantity.text[1:]), quest_name=quest_name.text, button_element=button,
                                  is_disable=button_status))
                    else:continue
                else:
                    #Nếu Quest là Coins
                    print(f"quantity item requirements : {int(quantity.text[1:])}")
                    print(f"id item requirements : {const.get_id_item(quest_name.text)}")
                    print(f"quest name requirements : {quest_name.text}")
                    total_value_coin_item = int(quantity.text[1:]) * get_price_item.get_price(id_item=const.get_id_item(quest_name.text),
                                                                      pid=const.ID_USER_REQUEST)

                    print(f"total $Coin quest: {quest_name.text} - {total_value_coin_item}")

                    if total_value_coin_item <= common_variables.TOTAL_LIMIT_COIN_QUEST:
                        try:
                            button.click()#Tra quest
                        except:
                            pass
                        quests.append(
                            Quest(quantity=int(quantity.text[1:]), quest_name=quest_name.text, button_element=button,
                                  is_disable=button_status))
                    else:continue
            except Exception as e:
                # traceback.print_exc()
                continue

        return quests

    def open_hazel_shop(self, driverControl: DriverControl) -> bool:
        actions = driverControl.action_chains()
        time.sleep(2)
        global is_open_list
        while True:
            try:
                screen_shot_path = f'{const.CURRENT_PATH_DIRECTORY}/images/hazel_quest/overview.png'
                driverControl.driver.save_screenshot(screen_shot_path)

                x, y = test.get_position(screen_shot_path,
                                         f'{const.CURRENT_PATH_DIRECTORY}/images/hazel_quest/list_hazel.png')

                actions.move_by_offset(x, y).click().perform()
                actions.move_by_offset(-x, -y).perform()
                is_open_list = driverControl.invisibility_of_element("Store_store-title__sJ_pw", "class")
                break
            except:
                time.sleep(0.15)
                continue
        if is_open_list:
            return True
        return False

    def buy_item(self, driverControl: DriverControl, quest: Quest):
        #reset value
        self.is_reload = False
        self.options_item_buy = []
        #---------------------------
        #if is_stop ís True -> Stop action and warning user
        if self.is_stop == True:
            return
        # ---------------------------

        actions = driverControl.action_chains()
        driver = driverControl.driver
        time.sleep(3)

        # find image and open market
        while True:
            try:
                screen_shot_path = f'{const.CURRENT_PATH_DIRECTORY}/images/hazel_quest/overview_open_market.png'
                driverControl.driver.save_screenshot(screen_shot_path)
                x, y = test.get_position(screen_shot_path,
                                         f'{const.CURRENT_PATH_DIRECTORY}/images/hazel_quest/enter_market.png')
                actions.move_by_offset(x, y).click().perform()
                actions.move_by_offset(-x, -y).perform()
                break
            except:
                time.sleep(0.2)
                continue
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

        # nhập item cần mua
        [filter_market_item.send_keys(i) for i in quest.quest_name]
        items = driver.find_elements(By.CLASS_NAME, 'Marketplace_item__l__LM')
        for item in items:
            #Duyệt danh sách các hàng hoá khác nhau, lấy ra hàng hoá có tên trùng nhau thì bấm mua
            # button_view_list = self.find_element_2_class('commons_pushbutton__7Tpa3', 'Marketplace_viewListings__q_KfD', item).click()
            # print("clicked", button_view_list, type(button_view_list))

            name = WebDriverWait(item, 30).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "Marketplace_itemName__Recoz")))
            # nếu tên trên list item trùng với item cần mua
            print(f"name.text >> {name.text} --- item_name >> {quest.quest_name}")
            if name.text == quest.quest_name:
                print("click button_lisst_view")
                button_view_list = self.find_element_2_class('commons_pushbutton__7Tpa3',
                                                             'Marketplace_viewListings__q_KfD', item)
                button_view_list.click()



                all_element_price = WebDriverWait(driver, 30).until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, 'MarketplaceItemListings_listing__TyllF'))
                )

                print("show lisst buy", type(all_element_price))
                for item_elem in all_element_price:
                    button = self.find_element_2_class('commons_pushbutton__7Tpa3','MarketplaceItemListings_buyListing__jYwuF',item_elem)


                    string_price = button.text
                    button_item_buy_status = button.get_attribute('disabled')
                    if button_item_buy_status is None:
                        string_price = string_price.replace(" ", "")
                        last_at_index = string_price.rfind("@")
                        if last_at_index == -1:
                            continue
                        last_colon_index = string_price.rfind(":", 0, last_at_index)

                        result = string_price[last_colon_index + 1: last_at_index]
                        print("result 1",result)

                        if result == "Allitem":
                            continue
                        print("result 2",result)
                        result.replace(',','') #vd số lượng "2,000" sẽ sai phải là '2000'
                        self.options_item_buy.append({"button": button, "quantity": int(result)})
                print("options: ",self.options_item_buy)
                # time.sleep(30)
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

                board_buy = driverControl.web_driver_wait('MarketplaceItemListings_content__eeHjR','class')

                number_item_bought = 0
                while True:
                    if self.is_reload == True:
                        #Nếu nhảy vào đây nghĩa là từng mua fail và cần reload lại list item để mua lại
                        actions.key_down(Keys.ESCAPE).perform()
                        time.sleep(0.5)
                        self.buy_item(driverControl,quest)
                        ##------------------------------
                    #---------------------------
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
                        #Nếu quá lâu không load ra hoặc tìm ra nut mua thì tải lại
                        self.is_reload = True
                        time.sleep(3)
                        continue

                    for button in button_but_or_not:
                        if 'Buy ' in button.text and 'for ' in button.text:
                            button.click()
                            print("check button -> buton.ettext", button.text)


                            print("clicked buy!")
                            try:
                                status_content = driverControl.web_driver_wait('Notifications_text__ak1FH',
                                                                                   'class')
                                if status_content.text == 'marketplace-purchase-failed':
                                    self.is_reload = True
                                    time.sleep(3)
                                    break
                                if status_content.text == 'Not enough space in inventory!':
                                    #Khong du chu mua do nua nen dung lai luon
                                    self.is_stop = True
                                    actions.key_down(Keys.ESCAPE).perform()
                                    time.sleep(2)
                                    return
                                    # self.buy_item(driverControl,quest)

                                else:
                                    suscess_inf = WebDriverWait(driver, 60).until(
                                        EC.visibility_of_all_elements_located((By.CLASS_NAME, "Marketplace_prop__fTsfy"))
                                    )
                                    for elmem in suscess_inf:
                                        if "Total in" in elmem.text:
                                            money_spend = elmem.text[8:].chuoi.replace(" ", "").replace("\n", "")
                                            # quantity_bought
                                            # print(f"total_in:{}- " )

                                    form_succes = driver.find_element(By.CLASS_NAME,'Marketplace_buttons__Imxzy')
                                    button = self.find_element_2_class('commons_uikit__Nmsxg ', 'commons_pushbutton__7Tpa3', form_succes)
                                    button.click()



                            except:
                                continue


                        # time.sleep(0.1)
                        if number_item_bought == quest.quantity:
                            break


                time.sleep(30)
                actions.key_down(Keys.ESCAPE).perform()

                break
            else:
                continue
        print("done??")
        time.sleep(100)

    def find_element_2_class(self, class1, class2, driver):
        try:
            elem = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, class1))
            )
        except:
            elem = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, class2))
            )
        return elem

    def find_elements_2_class(self, class1, class2, driver):
        try:
            elem = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, class1))
            )
        except:
            elem = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, class2))
            )
        return elem

