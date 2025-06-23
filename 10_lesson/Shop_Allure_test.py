import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from ShopPagesAllure.OpenShopAllure import OpenShop
from ShopPagesAllure.BasketShopAllure import Basket
from ShopPagesAllure.CheckProductShopAllure import CheckProduct
from ShopPagesAllure.YourInformationAllure import YourInformation
from ShopPagesAllure.CheckResultShopAllure import Result


@allure.feature("Тестирование онлайн-магазина")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест покупки товаров")
@allure.description("Тестирование процесса авторизации, "
                    "добавления товаров в корзину, "
                    "оформления заказа и проверки итоговой суммы заказа")
def test_shop():
    """Тест покупки товаров в интернет-магазине."""
    browser = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))

    with allure.step("Открытие сайта онлайн-магазина"):
        open = OpenShop(browser)
        open.avtorisation_login("standard_user")
        open.avtorisation_password("secret_sauce")
        open.click()

    with allure.step("Добавление товаров в корзину"):
        add_prod = Basket(browser)
        add_prod.add_product()
        add_prod.click_basket()

    with allure.step("Проверка доступных товаров"):
        check_prod = CheckProduct(browser)
        check_prod.check_product()
        check_prod.click_checkout()

    with allure.step("Заполнение информации о покупателе"):
        inform = YourInformation(browser)
        inform.add_information("Елена", "Елина", "310510")

    with allure.step("Проверка итоговой суммы заказа"):
        result = Result(browser)
        total = result.check_result()

    browser.quit()

    with allure.step("Проверка суммы"):
        assert total == "$58.29"
