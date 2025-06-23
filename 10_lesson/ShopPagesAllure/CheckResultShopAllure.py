import allure
from selenium.webdriver.common.by import By


class Result:
    """Класс для проверки итогов оформления заказа."""

    def __init__(self, browser):
        """Инициализация класса Result.
        Принимает параметр browser: WebDriver,
        экземпляр браузера для автоматизации."""
        self._driver = browser

    @allure.step
    def check_result(self) -> str:
        """Получение итоговой суммы заказа.
        Возвращает итоговую сумму заказа: str,
        строка с итоговой суммой заказа."""
        result = self._driver.find_element(
            By.CSS_SELECTOR, '[data-test="total-label"]').text
        total = result.replace("Total:", "").strip()
        return total
