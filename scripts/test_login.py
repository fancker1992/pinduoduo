import time

import pytest

from base.base_analyze import analyze_with_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def to_login_page(self):
        time.sleep(2)
        self.page.home.click_mine()
        time.sleep(2)
        self.page.mine.click_login_or_register()
        self.page.no_pwd_login.click_login_type()

    @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login"))
    def test_login(self, args):
        user_name = args["username"]
        password = args["password"]
        expect = args["expect"]
        self.to_login_page()
        self.page.login.input_user_name(user_name)
        self.page.login.input_pass_word(password)
        # self.page.login.click_login_btn()

    @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_logout"))
    def test_logout(self, args):
        username = args["username"]
        password = args["password"]
        self.to_login_page()
        self.page.login.input_user_name(username)
        self.page.login.input_pass_word(password)
        assert not self.page.login.is_button_enabled()
