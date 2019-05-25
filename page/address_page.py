from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressPage(BaseAction):
    add_btn = (By.XPATH, "//*[@text='添加收货地址' and @resource-id = 'com.yiwang:id/btn_add_address']")
    del_img = (By.ID, "com.yiwang:id/address_item_delete_img")
    dialog_ok_btn = (By.XPATH, "//*[@text='确定' and @resource-id = 'com.yiwang:id/dialog_btn_two']")

    def click_add_btn(self):
        self.click(self.add_btn)

    def click_del_img(self):
        self.click(self.del_img)

    def click_dialog_ok_btn(self):
        self.click(self.dialog_ok_btn)
