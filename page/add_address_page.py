import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddAddressPage(BaseAction):
    save_btn = (By.XPATH, "//*[@text='保存' and @resource-id='com.yiwang:id/title_right_content']")
    name_edit = (By.ID, "com.yiwang:id/add_address_real_name_et_id")
    phone_edit = (By.ID, "com.yiwang:id/add_address_real_phone_et_id")
    detail_address_edit = (By.ID, "com.yiwang:id/add_detail_address_et_id")
    check_box = (By.CLASS_NAME, "android.widget.CheckBox")
    select_address = (By.ID, "com.yiwang:id/add_address_select_area_id")
    address_list = (By.XPATH, "//*[@class='android.widget.ListView']/android.widget.RelativeLayout")

    def click_save_btn(self):
        self.click(self.save_btn)

    def input_name(self, text):
        self.input(self.name_edit, text)

    def input_phone(self, phone):
        self.input(self.phone_edit, phone)

    def input_detail_address(self, text):
        self.input(self.detail_address_edit, text)

    def click_check_box(self):
        self.click(self.check_box)

    def click_select_address(self):
        self.click(self.select_address)
        for i in range(4):
            address_list = self.find_elements(self.address_list)
            position = random.randint(0, len(address_list) - 1)
            address_list[position].click()
