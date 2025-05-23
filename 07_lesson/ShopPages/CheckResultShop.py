from selenium.webdriver.common.by import By


class Result:

    def __init__(self, browser):
        self._driver = browser

    def check_result(self):
        result = self._driver.find_element(
            By.CSS_SELECTOR, '[data-test="total-label"]').text
        total = result.replace("Total:", "").strip()
        return total
