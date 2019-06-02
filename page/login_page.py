from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    user_name_edit = (By.ID, "com.yiwang:id/et_username")
    pass_word_edit = (By.ID, "com.yiwang:id/et_password")
    login_btn = (By.ID, "com.yiwang:id/btn_login")

    def input_user_name(self, text):
        self.input(self.user_name_edit, text)

    def input_pass_word(self, text):
        self.input(self.pass_word_edit, text)

    def click_login_btn(self):
        self.click(self.login_btn)

    def is_button_enabled(self):
        self.is_enabled(self.login_btn)
