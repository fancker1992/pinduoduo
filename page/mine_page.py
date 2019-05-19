from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MinePage(BaseAction):
    setting_btn = (By.XPATH, "//*[@text = '设置']")

    def click_setting(self):
        self.click(self.setting_btn)
