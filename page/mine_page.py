from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MinePage(BaseAction):
    setting_btn = (By.XPATH, "//*[@text = '设置']")
    login_or_register = (By.ID, "com.yiwang:id/tv_username")

    def click_setting(self):
        self.click(self.setting_btn)

    def click_login_or_register(self):
        self.click(self.login_or_register)
