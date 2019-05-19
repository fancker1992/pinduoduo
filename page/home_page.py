from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    mine_btn = (By.XPATH, "//*[@text = '我的' and @resource-id = 'com.yiwang:id/navigation_user_tv']")

    def click_mine(self):
        self.click(self.mine_btn)
