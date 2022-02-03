import time

from ui.page.Basepage import Basepage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage(Basepage):
    def __init__(self, driver):
        super().__init__(driver)

    Login_button1 = "//*[@id='ifLoggedOut']"
    User_name = "//*[@id='un']"
    Password = "//*[@id='pw']"
    Remember_check_box = "input[name='rememberChkBox']"
    Login_window = "//*[@id='id01']/div/div"
    Remember_me_text = "span[class='rememberMe modalbottomtext upper']"
    Forgot_password = "#openerForgotPass"
    Login_button = "//*[@id='signin']"
    User_profile = "a[id ='userProfile']"
    Try_again_popup = "[class='sweet-alert showSweetAlert visible']"


    def is_login_button_exist(self):
        element = self.driver.find_element(By.XPATH, self.Login_button1).is_displayed()
        return element

    def click_on_login_button(self):
        element = self.driver.find_element(By.XPATH, self.Login_button1).click()


    def enter_user_name_and_password(self, enter_username, enter_password):
        self.driver.implicitly_wait(5)
        user_name = self.driver.find_element(By.XPATH, self.User_name).send_keys(enter_username)
        password = self.driver.find_element(By.XPATH, self.Password).send_keys(enter_password)

    def verify_the_remember_check_box(self):
        checkbox = self.driver.find_element(By.CSS_SELECTOR, self.Remember_check_box).click()

    def verify_login_winodw(self):
        self.driver.find_element(By.XPATH, self.Login_window).is_displayed()

    def verify_the_rememberme_text(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.Remember_me_text).text
        assert element == "REMEMBER ME"

    def forgot_password(self):
        element = self.driver.find_element(By.CSS_SELECTOR,self.Forgot_password).text
        assert element == "FORGOT PASSWORD?"

    def press_login_button(self):
       button_text = self.driver.find_element(By.XPATH,self.Login_button).text
       assert button_text == "LOG IN"
       self.driver.find_element(By.XPATH,self.Login_button).click()


    def verify_login_user_profile(self):
        profile = self.driver.find_element(By.CSS_SELECTOR,self.User_profile).text
        try :
            assert profile == "Hi, PLAYER001"
            print("PASS!!!!!!!Sucessfully login Account!!!")
        except:
            print("FAIL!!!!!!Not able to login Account!!!")

    def verfiy_try_again_popup(self):
        popup = self.driver.find_element(By.CSS_SELECTOR,self.Try_again_popup).text
        print("POPUP VERIFIED!!!!!!!!!!!!!-",popup)
        time.sleep(3)
        if popup == "Please check the password and try again.":
            print("PASS!!!! GETTING TRY AGAIN POPUP!!!!!!")


