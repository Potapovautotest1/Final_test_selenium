from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), 'there is not Login form'

        
    def should_be_register_form(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), 'there is not register form'
        assert True
       
    def should_be_register_form1(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        
    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str('Qyjy1289hg1')
        registration_form_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        registration_form_email.send_keys(email)
        registration_form_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        registration_form_password1.send_keys(password)
        registration_form_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        registration_form_password2.send_keys(password)
        btn_to_registr = self.browser.find_element(*LoginPageLocators.BTN_REGISTR)
        btn_to_registr.click()
        time.sleep(5)

        
