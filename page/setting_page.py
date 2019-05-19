from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):
    address_manager = (By.XPATH, "//*[@text='地址管理']")

    def click_address_manager(self):
        self.click(self.address_manager)
