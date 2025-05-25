from selenium.webdriver.common.by import By


class CheckProduct:

    def __init__(self, browser):
        self._driver = browser

    def check_product(self):
        self._driver.find_element(
            By.XPATH, '//div[text() = "Sauce Labs Bolt T-Shirt"]')
        self._driver.find_element(
            By.XPATH, '//div[text() = "Sauce Labs Onesie"]')
        self._driver.find_element(
            By.XPATH, '//div[text() = "Sauce Labs Backpack"]')

    def click_checkout(self):
        self._driver.find_element(By.ID, "checkout").click()
