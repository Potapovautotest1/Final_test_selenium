from pages.base_page import BasePage
from pages.locators import Addtobasket
from selenium.common.exceptions import NoAlertPresentException
import time

class BasketPage(BasePage):
    def test_quest_cant_see_product_in_basket(self):
        assert self.is_not_element_present(*Addtobasket.BASKET_ITEMS), "Success message is presented"       
     