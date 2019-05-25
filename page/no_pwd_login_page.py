from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NoPwdLoginPage(BaseAction):
    login_type = (By.ID, "com.yiwang:id/tv_login_type")

    def click_login_type(self):
        self.click(self.login_type)
