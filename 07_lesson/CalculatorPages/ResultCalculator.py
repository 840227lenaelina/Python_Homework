from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultCalculatop():

    def __init__(self, browser):
        self._driver = browser

    def input_date(self):
        self._driver.find_element(By.XPATH, '//span[text()= "7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()= "8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()= "="]').click()

    def result(self):
        result_log = (By.XPATH, '//div[text() = "15"]')
        result1 = WebDriverWait(self._driver, 46, 1).until(
            EC.visibility_of_element_located(result_log))
        return int(result1.text)
