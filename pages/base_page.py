import math
import time
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.locators import Addtobasket
from pages.locators import LoginPageLocators
from selenium.common.exceptions import TimeoutException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url) 
        
        
    def go_to_basket(self):
        go_to_basket = self.browser.find_element(*Addtobasket.BTN_GO_BASKET)
        go_to_basket.click()
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        print(x)
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(answer)
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        
    def btn_to_basket(self):
        login_link = self.browser.find_element(*Addtobasket.BTN_ADD_BASKET)
        login_link.click()

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
        
        
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
        
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except:
            return False
        return True
        
    def go_to_home_page(self):
        go_to_home_page = self.browser.find_element(*Addtobasket.HOME_PAGE)
        go_to_home_page.click()
        
    def should_be_authorized_user(self):
        assert self.is_element_present(*Addtobasket.USER)