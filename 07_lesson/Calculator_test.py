from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from CalculatorPages.MainPageCalculator import MainPageCalc
from CalculatorPages.ResultCalculator import ResultCalculatop


def test_calculator():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    main_calcul = MainPageCalc(browser)
    main_calcul.search("45")

    result_sum = ResultCalculatop(browser)
    result_sum.input_date()
    to_as = result_sum.result()
    assert to_as == 15

    browser.quit()
