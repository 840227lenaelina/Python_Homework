from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

search_input = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
search_input.send_keys("Sky")

sleep(5)

search_input.clear()

sleep(5)

search_input.send_keys("Pro")

sleep(5)

driver.quit()
