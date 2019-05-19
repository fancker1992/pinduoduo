from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressManger(BaseAction):
    edit_btn = (By.XPATH, "//*[@text = '编辑' and @resource-id = 'com.ddsy.songyao:id/modify']")

    def click_edit(self):
        self.click(self.edit_btn)
