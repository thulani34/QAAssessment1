import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_factorial_of_7():
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(2)
    driver.get("http://localhost:6464/")
    driver.find_element(By.CSS_SELECTOR, '#number').send_keys('7')
    driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
    time.sleep(3)
    element = driver.find_element(By.XPATH, "//p[@id='resultDiv']")
    assert element.text == 'The factorial of 7 is: 5040'
    time.sleep(3)
    driver.quit()
