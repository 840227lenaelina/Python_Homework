from selenium.webdriver.common.by import By


class MainPageCalc:

    def __init__(self, browser):
        self._driver = browser
        self._driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def search(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.ID, "delay").send_keys(term)
