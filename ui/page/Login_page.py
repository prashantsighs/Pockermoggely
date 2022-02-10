import logging
import time
import unittest
from ui.page.Basepage import Basepage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ui.data.config import Testdata
from ui.page.Home_page import HomePage

class LoginPage(Basepage, Testdata):
    def __init__(self, driver):
        super().__init__(driver)

    Login_button1 = (By.XPATH,"//*[@id='ifLoggedOut']")
    User_name = (By.XPATH,"//*[@id='un']")
    Password = (By.XPATH,"//*[@id='pw']")
    Remember_check_box = (By.CSS_SELECTOR,"input[name='rememberChkBox']")
    Login_window = (By.XPATH,"//*[@id='id01']/div/div")
    Remember_me_text = (By.CSS_SELECTOR,"span[class='rememberMe modalbottomtext upper']")
    Forgot_password = (By.CSS_SELECTOR,"#openerForgotPass")
    Login_button = (By.XPATH,"//*[@id='signin']")
    User_profile = (By.CSS_SELECTOR,"a[id ='userProfile']")
    Try_again_popup = (By.CSS_SELECTOR,"[class='sweet-alert showSweetAlert visible']")
    Log_out_button = (By.XPATH,"//*[contains(@class,'tlink upper robotoc')]")

    def is_login_button_exist(self):

        element = self.is_visible(self.Login_button1)
        return element

    def click_on_login_button(self):

        self.do_click(self.Login_button1)

    def enter_user_name_and_password(self, enter_username, enter_password):
        self.driver.implicitly_wait(5)
        user_name = self.do_send_key(self.User_name,enter_username)
        password = self.do_send_key(self.Password,enter_password)

    def verify_the_remember_check_box(self):
        checkbox = self.select_the_element(self.Remember_check_box)


    def verify_login_winodw(self):

         self.is_visible(self.Login_window)

    def verify_the_rememberme_text(self):
        element = self.get_element_text(self.Remember_me_text)
        assert element == "REMEMBER ME"

    def forgot_password(self):
        element = self.get_element_text(self.Forgot_password)
        assert element == "FORGOT PASSWORD?"

    def press_login_button(self):
        button_text = self.get_element_text(self.Login_button)
        assert button_text == "LOG IN"
        self.do_click(self.Login_button)


    def verify_login_user_profile(self):
        profile = self.get_element_text(self.User_profile)
        try:
            assert profile == "Hi, PLAYER001"
            print("PASS!!!!!!!Sucessfully login Account!!!")
        except:
            print("FAIL!!!!!!Not able to login Account!!!")

    def verfiy_try_again_popup(self):

        Actual_alert = self.get_element_text(self.Try_again_popup)
        import logging
        logging.info("THE $$$$$$$$$$$$$$$$$$$$$$",Actual_alert)
        time.sleep(3)
        for alert in self.Expected_alerts:
            if alert == Actual_alert:
                assert alert == Actual_alert
                print("PASS", "Alert is", Actual_alert)


    def verify_and_click_on_log_out_button(self):
        logout_print = self.get_element_text(self.Log_out_button)
        assert logout_print == "LOGOUT" ,"Not able to find the LOGOUT BUTTON"
        print("Able to see the logout button", logout_print)
        click_on_logout = self.do_click(self.Log_out_button)


    def verify_that_application_logout(self):
        self.is_login_button_exist()
