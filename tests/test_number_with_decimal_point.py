import sys
import time
from io import StringIO

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_number_with_decimal_point():
    # initialising chrome
    driver = webdriver.Chrome()
    time.sleep(2)
    driver.get("http://localhost:6464/")
    assert "Factoriall" in driver.title
    driver.find_element(By.CSS_SELECTOR, '#number').send_keys('7.01')
    driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
    time.sleep(2)
    element = driver.find_element(By.XPATH, "//p[@id='resultDiv']")
    assert element.text == 'Please enter an integer'
    time.sleep(2)
    # Quit the driver
    driver.quit()