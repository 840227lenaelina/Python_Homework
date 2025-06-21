import allure
from selenium.webdriver.common.by import By


class CheckProduct:
    """Класс для проверки наличия выбранных товаров в корзине
     и перехода к оформлению заказа"""

    def __init__(self, browser):
        """Инициализация класса OpenShop.
        Принимает параметр browser: WebDriver,
        экземпляр браузера для автоматизации."""
        self._driver = browser

    @allure.step
    def check_product(self) -> None:
        """Проверка наличия определенных товаров на странице."""
        self._driver.find_element(By.XPATH,
                                  '//div[text() = "Sauce Labs Bolt T-Shirt"]')
        self._driver.find_element(By.XPATH,
                                  '//div[text() = "Sauce Labs Onesie"]')
        self._driver.find_element(By.XPATH,
                                  '//div[text() = "Sauce Labs Backpack"]')

    @allure.step
    def click_checkout(self) -> None:
        """Клик по кнопке 'Checkout' для перехода к оформлению заказа."""
        self._driver.find_element(By.ID, "checkout").click()
