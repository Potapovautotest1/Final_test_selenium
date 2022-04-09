from pages.base_page import BasePage
from pages.locators import Addtobasket
from selenium.common.exceptions import NoAlertPresentException
import time

class Add_to_basket(BasePage):
    def name_price_in_home_page(self):
        global n
        global p
        name_home_page = self.browser.find_element(*Addtobasket.NAME)
        n = name_home_page.text
        price_home_page = self.browser.find_element(*Addtobasket.PRICE_HOME_PAGE)
        p = price_home_page.text

    def name_price_in_basket(self):
        global n_b
        global p_b
        name_in_basket = self.browser.find_element(*Addtobasket.NAME_IN_BASKET)
        n_b = name_in_basket.text
        price_in_basket = self.browser.find_element(*Addtobasket.PRICE_IN_BASKET)
        p_b = price_in_basket.text


    def assert_name_price(self):
        assert n == n_b, 'Название товара в корзине не совпадает с названием на главной странице'
        assert p == p_b, 'Цена товара в корзине не совпадает с ценой на главной странице'
     
     
    def test_quest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*Addtobasket.SUCCES_MESSAGE), "Success message is presented"
        
        
    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*Addtobasket.SUCCES_MESSAGE), "Success message is presented"
        
    
    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*Addtobasket.SUCCES_MESSAGE), "Success message is presented"    
     