from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest

@pytest.mark.login_quest
class TestLoginFromMainPage():
    def test_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
    
    
    def test_guest_should_see_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()