from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")


class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_OF_GOOD = (By.CSS_SELECTOR, ".product_main > .price_color")
    NAME_OF_GOOD = (By.CSS_SELECTOR, ".product_main > h1")
    NAME_OF_GOOD_IN_ALERT = (By.CSS_SELECTOR, "#messages > :nth-child(1) strong")
    PRICE_OF_GOOD_IN_ALERT = (By.CSS_SELECTOR, "#messages > :nth-child(3) strong")
