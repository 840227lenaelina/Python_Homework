1. Для работы с проектами необходимо произвести установку и настройку:
1.1. Установите зависимости
Для работы с проектом вам понадобятся следующие зависимости:
Python 3.13
Selenium
Webdriver Manager
Allure Pytest
Создайте виртуальное окружение и установите зависимости из файла requirements.txt.(команда pip install -r requirements.txt)
2. Для запуска тестов: Выполните команду pytest -k 10_lesson
3. Для генерации отчетов Allure:
3.1. Выполните команду: pytest --alluredir allure-result 10_lesson - для формирования отчета о тестировании
3.2. Затем выполните команду: allure serve allure-result - для генерации отчета и вывода результатов
4. Тестирование проводится для 2-х проектов:

4.1. **Проект Calculator** - тестирование калькулятора, содержит:

4.1.1. Директорию CalculatorPagesAllure в которой находится 
файл класса ResultCalculatorAllure.py, использующий следующие методы:
- _init_(self, browser: WebDriver): Для инициализация класса. 
Открывает страницу калькулятора.
- search(self, term: str) -> None: Вводит задержку в калькуляторе.
- input_data(self, first_value: int, operator: str, second_value: int) -> None: 
Вводит данные для вычисления.
- result(self) -> int: Получает результат вычисления.
4.1.2. Файл для тестирования Calculator_Allure_test.py, содержащий в себе тест на вычисление суммы для чисел 7 и 8 
и сравнения её с ожидаемым результатом.

4.2. **Проект Shop** - тестирование онлайн-магазина, содержит в себе:

4.2.1. Директорию ShopPagesAllure в которой находятся следующие файлы класса:
4.2.1.1. OpenShopAllure.py с методами:
- _init_(self, browser: WebDriver): Для инициализация класса. 
- avtorisation_login(self, login: str) -> None: Для ввода логина.
- avtorisation_password(self, password: str) -> None: Для ввода пароля.
- click(self) -> None: Для клика по кнопке, осуществляющей вход в систему
4.2.1.2.BasketShopAllure.py с методами:
- _init_(self, browser: WebDriver): Для инициализация класса.
- add_product(self) -> None: Для добавления продуктов в корзину.
- def click_basket(self) -> None: Для клика по значку корзины и осуществление перехода в корзину.
4.2.1.3. CheckProductShopAllure.py с методами:
- _init_(self, browser: WebDriver): Для инициализация класса.
- check_product(self) -> None: Для проверки наличия продуктов в корзине.
- click_checkout(self) -> None: Для клика по кнопке 'Checkout' и перехода к оформлению заказа.
4.2.1.4. YourInformationAllure.py с методами:
- _init_(self, browser: WebDriver): Для инициализация класса. 
- add_information(self, first_name: str, last_name: str, postal_code: str) -> None:
Для заполнения информации о покупателе и перехода 
на страницу с суммой заказа
4.2.1.5. CheckResultShopAllure.py с методами:
- _init_(self, browser: WebDriver): Для инициализация класса. 
- check_result(self) -> str:Для получения итоговой суммы заказа.
4.2.2. Файл для тестирования Shop_Allure_test.py, содержащий в себе тест для проверки
входа на сайт онлайн-магазина, выбора товаров, проверки наличия товаров в корзине, 
ввода информации о покупателе и соответствия суммы ожидаемому результату.
5. Каждый шаг теста помечен с помощью Allure, 
что позволяет более удобно отслеживать выполнение тестов и их результаты.