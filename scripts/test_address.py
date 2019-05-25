import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from base.base_driver import init_driver
from page.page import Page


class TestAddress:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_add_address(self):
        time.sleep(2)
        self.page.home.click_mine()
        time.sleep(2)
        TouchAction(self.driver).tap(x=1000, y=133).perform()  # 点击设置
        # self.page.mine.click_setting()
        self.page.setting.click_address_manager()
        self.page.address.click_add_btn()
        self.page.add_address.input_name("大熊")
        self.page.add_address.input_phone("15101006426")
        self.page.add_address.click_select_address()
        self.page.add_address.input_detail_address("田园小区一号楼")
        # self.page.add_address.click_check_box()
        self.page.add_address.click_save_btn()
        res = self.page.address.find_toast("成功")
        print(res)

        assert "成功" in res
