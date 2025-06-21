import allure
from selenium.webdriver.common.by import By


class OpenShop:
    """Класс содержит функции для открытия сайта онлайн-магазина."""

    def __init__(self, browser):
        """Инициализация класса OpenShop.
        Принимает параметр browser: WebDriver,
        экземпляр браузера для автоматизации."""
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step
    def avtorisation_login(self, login: str) -> None:
        """Ввод логина на странице авторизации.
        Принимает на вход параметр login: str, имя пользователя для входа."""
        self._driver.find_element(By.ID, "user-name").send_keys(login)

    @allure.step
    def avtorisation_password(self, password: str) -> None:
        """Ввод пароля на странице авторизации.
        Принимает на вход параметр password: str, пароль для входа."""
        self._driver.find_element(By.ID, "password").send_keys(password)

    @allure.step
    def click(self) -> None:
        """Клик по кнопке 'Login' для входа в систему."""
        self._driver.find_element(By.ID, "login-button").click()
