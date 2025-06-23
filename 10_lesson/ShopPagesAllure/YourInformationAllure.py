import allure
from selenium.webdriver.common.by import By


class YourInformation:
    """Класс для заполнения информации о покупателе."""

    def __init__(self, browser):
        """Инициализация класса YourInformation.
        Принимает параметр browser: WebDriver,
        экземпляр браузера для автоматизации."""
        self._driver = browser

    @allure.step
    def add_information(self, first_name: str,
                        last_name: str, postal_code: str) -> None:
        """Заполнение информации о покупателе."""
        self._driver.find_element(By.ID, "first-name").send_keys(first_name)
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)
        self._driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self._driver.find_element(By.ID, "continue").click()
