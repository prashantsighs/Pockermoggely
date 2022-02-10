import logging

import pytest
from ui.page.Login_page import LoginPage
from ui.tests.generic import setup
from ui.tests.test_baseclass import Baseclass
from ui.data.config import Testdata
from ui.page.Home_page import HomePage


class Testcases(Baseclass,Testdata):



    def test_login_the_poker_moggelly_by_right_username_and_right_password(self):
       self.login = LoginPage(self.driver)
       flag = self.login.is_login_button_exist()
       assert flag
       self.login.click_on_login_button()
       self.login.verify_login_winodw()
       self.login.enter_user_name_and_password("Player001", "111111")
       self.login.verify_the_rememberme_text()
       self.login.verify_the_remember_check_box()
       self.login.press_login_button()
       self.login.verify_login_user_profile()

    def test_login_the_poker_moggelly_by_right_username_and_wrong_password(self):
        self.login = LoginPage(self.driver)
        self.driver.implicitly_wait(5)
        flag = self.login.is_login_button_exist()
        assert flag
        self.login.click_on_login_button()
        self.login.verify_login_winodw()
        self.login.enter_user_name_and_password("Player001", "222222")
        self.login.press_login_button()
        self.login.verfiy_try_again_popup()


    def test_login_the_poker_moggelly_by_user_name_special_characher_and_wrong_password(self):
        self.login = LoginPage(self.driver)
        self.driver.implicitly_wait(5)
        flag = self.login.is_login_button_exist()
        assert flag
        self.login.click_on_login_button()
        self.login.verify_login_winodw()
        self.login.enter_user_name_and_password("@@@@@@", "222222")
        self.login.press_login_button()
        self.login.verfiy_try_again_popup()

    def test_login_the_poker_moggelly_by_invalid_user_name_and_right_password(self):
        self.login = LoginPage(self.driver)
        self.driver.implicitly_wait(5)
        flag = self.login.is_login_button_exist()
        assert flag
        self.login.click_on_login_button()
        #logging.INFO("DFEGVFUGYEGVFUYUFGEFUYGFIFIUEFGIF")
        self.login.verify_login_winodw()
        self.login.enter_user_name_and_password("222222", "222222")
        self.login.press_login_button()
        self.login.verfiy_try_again_popup()

    def test_the_logout_option_on_homepage(self):
        self.test_login_the_poker_moggelly_by_right_username_and_right_password()
        self.login.verify_and_click_on_log_out_button()
        self.login.verify_that_application_logout()




