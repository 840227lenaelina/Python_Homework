from selenium.webdriver.common.by import By


class Basket:

    def __init__(self, browser):
        self._driver = browser

    def add_product(self):
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    def click_basket(self):
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
