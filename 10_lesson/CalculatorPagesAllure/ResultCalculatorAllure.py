import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    """Класс для работы с калькулятором на странице."""

    def __init__(self, browser):
        """Инициализация класса Calculator.
        Принимает параметр browser: WebDriver,
        браузер для автоматизации."""
        self._driver = browser
        self._driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Поиск элемента для ввода задержки")
    def search(self, term: str) -> None:
        """Ввод задержки вывода результата в калькуляторе.
            Принимает на вход параметр term: str, значение задержки."""
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.ID, "delay").send_keys(term)

    @allure.step("Ввод данных для подсчета")
    def input_data(self, first_value: int, operator: str,
                   second_value: int) -> None:
        """Ввод первых чисел и оператора,
            затем вторых чисел для вычисления.
            Принимает параметр first_value: int,
            первое число для операции.
            Принимает параметр operator: str,
            оператор (например, "+", "-", "*", "/").
            Принимает параметр second_value: int, второе число для операции."""
        for digit in str(first_value):
            self._driver.find_element(By.XPATH,
                                      f'//span[text()="{digit}"]').click()
        self._driver.find_element(By.XPATH,
                                  f'//span[text()="{operator}"]').click()
        for digit in str(second_value):
            self._driver.find_element(By.XPATH,
                                      f'//span[text()="{digit}"]').click()
            self._driver.find_element(By.XPATH, '//span[text()="="]').click()

    @allure.step("Получение результата")
    def result(self) -> int:
        """Получение результата вычисления.
            Возвращает параметр: int,
            результат вычисления."""
        result_log = (By.XPATH, '//div[text() = "15"]')
        result1 = WebDriverWait(self._driver, 46, 1).until(
                EC.visibility_of_element_located(result_log))
        return int(result1.text)
