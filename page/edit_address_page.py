from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class EditAddressPage(BaseAction):
    save_btn = (By.ID, "com.ddsy.songyao:id/save")

    def click_save(self):
        self.click(self.save_btn)
