from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("http://the-internet.herokuapp.com/login")

search_name_loc = ("xpath", '//input[@name="username"]')
search_name = wait.until(EC.visibility_of_element_located(search_name_loc))
search_name.send_keys("tomsmith")

search_password_loc = ("xpath", '//input[@name="password"]')
search_password = wait.until(
    EC.visibility_of_element_located(search_password_loc))
search_password.send_keys("SuperSecretPassword!")

search_button_loc = ("xpath", '//button[@class="radius"]')
search_button = wait.until(EC.visibility_of_element_located(search_button_loc))
search_button.click()

text_loc = ("xpath", '//div[@id="flash"]')
text = wait.until(EC.visibility_of_element_located(text_loc))
text_1 = text.text
print(text_1[:-1])

driver.quit()
