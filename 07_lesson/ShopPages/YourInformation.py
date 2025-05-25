from selenium.webdriver.common.by import By


class YourInformation:

    def __init__(self, browser):
        self._driver = browser

    def add_information(self):
        self._driver.find_element(By.ID, "first-name").send_keys("Елена")
        self._driver.find_element(By.ID, "last-name").send_keys("Елина")
        self._driver.find_element(By.ID, "postal-code").send_keys("310510")
        self._driver.find_element(By.ID, "continue").click()
