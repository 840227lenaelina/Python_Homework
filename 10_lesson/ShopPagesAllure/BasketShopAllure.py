import allure
from selenium.webdriver.common.by import By


class Basket:
    """Класс содержит функции для поиска и выбора продукции на сайте
    и добавления выбранных товаров в корзину"""

    def __init__(self, browser):
        """Инициализация класса Basket.
        Принимает параметр browser: WebDriver,
        экземпляр браузера для автоматизации."""
        self._driver = browser

    @allure.step
    def add_product(self) -> None:
        """Добавление продуктов в корзину."""
        self._driver.find_element(By.ID,
                                  "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.ID,
                                  "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.ID,
                                  "add-to-cart-sauce-labs-onesie").click()

    @allure.step
    def click_basket(self) -> None:
        """Клик по иконке корзины для просмотра добавленных товаров."""
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
