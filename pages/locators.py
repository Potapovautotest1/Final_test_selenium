from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
     
     
class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")  
    PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")    
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")  
    BTN_REGISTR = (By.NAME, "registration_submit") 
    
    
class Addtobasket:
    USER = (By.CSS_SELECTOR, ".icon-user")  
    BTN_ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BTN_GO_BASKET = (By.CSS_SELECTOR, ".btn-group")
    NAME_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4 h3 a")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "h3.price_color")
    PRICE_HOME_PAGE = (By.CSS_SELECTOR, ".price_color:nth-child(2)")
    SUCCES_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1)")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    HOME_PAGE = (By.CSS_SELECTOR, ".col-sm-7 a")
