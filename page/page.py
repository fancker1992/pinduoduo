from page.add_address_page import AddAddressPage
from page.address_page import AddressPage
from page.edit_address_page import EditAddressPage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.mine_page import MinePage
from page.no_pwd_login_page import NoPwdLoginPage
from page.setting_page import SettingPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def mine(self):
        return MinePage(self.driver)

    @property
    def setting(self):
        return SettingPage(self.driver)

    @property
    def edit_address(self):
        return EditAddressPage(self.driver)

    @property
    def address(self):
        return AddressPage(self.driver)

    @property
    def add_address(self):
        return AddAddressPage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def no_pwd_login(self):
        return NoPwdLoginPage(self.driver)
