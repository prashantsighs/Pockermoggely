import pytest
from ui.page.Login_page import LoginPage
from ui.tests.generic import setup
from ui.tests.test_baseclass import Baseclass
from ui.data.config import Testdata
from ui.tests.test_login import Testcases
from ui.page.Home_page import HomePage
from ui.page.Basepage import Basepage
from selenium.webdriver.common.by import By


class TestHomePage(Testcases):




    testcase = Testcases()
    def test_the_download_plateform(self):
        self.login = LoginPage(self.driver)
        flag = self.login.is_login_button_exist()
        assert flag
        self.login.click_on_login_button()
        self.login.verify_login_winodw()
        self.login.enter_user_name_and_password("Player001", "111111")
        self.login.verify_the_rememberme_text()
        self.login.verify_the_remember_check_box()
        self.login.press_login_button()
        self.home = HomePage(self.driver)
        self.home.verify_the_all_plateform()

    def test_the_logout_option_on_homepage(self):

        self.testcase.test_login_the_poker_moggelly_by_right_username_and_right_password()
        self.login.verify_and_click_on_log_out_button()
        self.login.verify_that_application_logout()


    def test_verify_the_performance_board(self):
        self.login = LoginPage(self.driver)
        flag = self.login.is_login_button_exist()
        assert flag
        self.login.click_on_login_button()
        self.login.verify_login_winodw()
        self.login.enter_user_name_and_password("Player001", "111111")
        self.login.verify_the_rememberme_text()
        self.login.verify_the_remember_check_box()
        self.login.press_login_button()
        self.home = HomePage(self.driver)
        self.home.verify_the_level()
        self.home.verify_the_locked_bonus()


    def test_verify_the_main_menu_items(self):
        self.login = LoginPage(self.driver)
        flag = self.login.is_login_button_exist()
        assert flag
        self.login.click_on_login_button()
        self.login.verify_login_winodw()
        self.login.enter_user_name_and_password("Player001", "111111")
        self.login.press_login_button()
        self.home = HomePage(self.driver)
        self.home.verify_the_main_menu_options()
        self.home.verify_the_chips_details()

    def test_fill_the_Player_Profile(self):
        self.login = LoginPage(self.driver)
        flag = self.login.is_login_button_exist()
        assert flag
        self.login.click_on_login_button()
        self.login.verify_login_winodw()
        self.login.enter_user_name_and_password("Player001", "111111")
        self.login.press_login_button()
        self.basepage = Basepage(self.driver)
        self.basepage.do_click(self.Profile)
