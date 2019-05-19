from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressPage(BaseAction):
    add_btn = (By.XPATH, "//*[@text='添加收货地址' and @resource-id = 'com.yiwang:id/btn_add_address']")

    def click_add_btn(self):
        self.click(self.add_btn)
