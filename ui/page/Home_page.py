import logging
import time
import unittest
from ui.page.Basepage import Basepage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ui.data.config import Testdata
import logging
from logging import getLogger



class HomePage(Basepage,Testdata):
    def __init__(self, driver):
        super().__init__(driver)

    Build_plate_from = "//*[@id='downloadApps']/div[2]"
    Level = "//*[@id='account']/div[3]/div[1]"
    Locked_bonus = "//*[@id='account']/div[3]/div[2]"
    Main_Menu = '//*[@id="cash-buttons-main"]'
    Chips_details =  ".heading"


    def verify_the_all_plateform(self):
        details = self.driver.find_element(By.XPATH, self.Build_plate_from).text
        print(details, )
        assert "INSTANT PLAY" in details

    def verify_the_level(self):
        level = self.driver.find_element(By.XPATH, self.Level).text
        print(level)
        log = getLogger()
        log.info("level is ", level)

       # assert level == ''' VIP LEVEL
        #                    Bronze '''

    def verify_the_locked_bonus(self):
        bonus = self.driver.find_element(By.XPATH,self.Locked_bonus).text
        print(bonus)

    def verify_the_main_menu_options(self):
        main_menu = self.driver.find_elements(By.XPATH,self.Main_Menu)
        MENU_LIST = []
        for item in main_menu:

            actual_main_menu_list = item.text
            print(actual_main_menu_list)
            assert actual_main_menu_list == self.Main_menu_expected_options
        print("PASS")

    def verify_the_chips_details(self):
        CHIPS = self.driver.find_elements(By.CSS_SELECTOR,self.Chips_details)
        CHIP_LIST = []
        for chips in CHIPS:
            ch = chips.text
            if ch in self.CHIPS_DETAILS:
                print("THE CHIPS DETAILS ARE AS EXPECTED",ch)