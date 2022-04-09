from pages.locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        
        
    def should_be_login_link(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_LINK)