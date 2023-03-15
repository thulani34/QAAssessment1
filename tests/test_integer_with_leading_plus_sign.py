import sys
import time
from io import StringIO

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_integer_with_leading_plus_sign():
    # initialising chrome
    driver = webdriver.Chrome()
    # calling url required
    time.sleep(2)
    driver.get("http://localhost:6464/")
    assert "Factoriall" in driver.title
    driver.find_element(By.CSS_SELECTOR, '#number').send_keys('+++7')
    driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
    time.sleep(2)
    element = driver.find_element(By.XPATH, "//p[@id='resultDiv']")
    assert element.text == 'Please enter an integer'
    driver.quit()
