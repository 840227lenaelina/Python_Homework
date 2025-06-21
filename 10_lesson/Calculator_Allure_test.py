import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from CalculatorPagesAllure.ResultCalculatorAllure import Calculator


@allure.feature("Тестирование калькулятора")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест вычисления суммы")
@allure.description("Тестирование работы калькулятора с операцией сложения.")
def test_result():
    """Тест вычисления результата 7 + 8 в калькуляторе."""
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    with allure.step("Инициализация калькулятора"):
        main_calcul = Calculator(browser)

    with allure.step("Установка задержки"):
        main_calcul.search("45")

    with allure.step("Ввод данных для вычисления"):
        main_calcul.input_data(7, "+", 8)  # Вводим 7 + 8

    with allure.step("Получение и проверка результата"):
        result_sum = main_calcul.result()
        assert result_sum == 15

    browser.quit()
