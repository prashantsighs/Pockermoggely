from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Basepage():
    def __init__(self,driver):
        self.driver = driver

    def do_click(self,By_locater):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(By_locater)).click()


    def do_send_key(self,By_locater,text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By_locater)).send_keys(text)


    def get_element_text(self,By_locater):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(By_locater))
        return element.text()

    def is_visible(self,By_locater):
        element = WebDriverWait(self.driver,10)
        element.until(EC.visibility_of_element_located(By_locater))
       # return bool(element)

    def select_the_element(self,By_locater):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By_locater)).click()