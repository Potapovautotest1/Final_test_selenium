from pages.product_page import Add_to_basket
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException
import pytest
import time

    
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = Add_to_basket(browser, link)
    page.open()
    page.btn_to_basket() 
    time.sleep(5)
    page.name_price_in_home_page()
    page.go_to_basket()
    page.name_price_in_basket()
    page.assert_name_price()
    time.sleep(3) 


@pytest.mark.need_review
class TestUserCanAddProductToBasket():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_register_form1()
        page.register_new_user()
        time.sleep(5)
        page.should_be_authorized_user() 
        
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = Add_to_basket(browser, link)
        page.open()
        page.btn_to_basket() 
        time.sleep(5)
        page.name_price_in_home_page()
        page.go_to_basket()
        page.name_price_in_basket()
        page.assert_name_price()
        time.sleep(3)  

@pytest.mark.need_review
def test_quest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()     


@pytest.mark.need_review
def test_quest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = LoginPage(browser, link)
    basket = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    basket.test_quest_cant_see_product_in_basket()
    





#Прочие тесты

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_can_add_product_to_basket(browser, link):
    page = Add_to_basket(browser, link)
    page.open()
    page.btn_to_basket() 
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.name_price_in_home_page()
    page.go_to_basket()
    page.name_price_in_basket()
    page.assert_name_price()
    time.sleep(3)   
    

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = Add_to_basket(browser, link)
    page.open()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.name_price_in_home_page()
    page.go_to_basket()
    page.name_price_in_basket()
    page.assert_name_price()
    time.sleep(3)   
    
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_quest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = Add_to_basket(browser, link)
    page.open()
    page.btn_to_basket() 
    page.test_quest_cant_see_success_message_after_adding_product_to_basket()
    
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])   
def test_guest_cant_see_success(browser, link):
    page = Add_to_basket(browser, link)
    page.open()
    page.test_guest_cant_see_success_message()
 
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"]) 
def test_message_disappeared_after_adding_product_to_b(browser, link):
    page = Add_to_basket(browser, link)
    page.open() 
    page.btn_to_basket()    
    page.test_message_disappeared_after_adding_product_to_basket()     
    
@pytest.mark.user
class TestUserAddToBasketFromProductPage():   
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_register_form1()
        page.register_new_user()
        time.sleep(5)
        page.should_be_authorized_user() 
        
    def test_user_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link)
        basket = BasketPage(browser, link)
        page.go_to_home_page()
        page.go_to_basket()
        basket.test_quest_cant_see_product_in_basket()    

    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link)
        basket = BasketPage(browser, link)
        page.go_to_basket()
        basket.test_quest_cant_see_product_in_basket()