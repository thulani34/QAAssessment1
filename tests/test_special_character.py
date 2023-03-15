import sys
from io import StringIO

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_special_character():
    # initialising chrome
    driver = webdriver.Chrome()
    # calling url required
    driver.get("http://localhost:6464/")
    driver.find_element(By.CSS_SELECTOR, '#number').send_keys('@#$%^&')
    driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
    element = driver.find_element(By.XPATH, "//p[@id='resultDiv']")
    assert element.text == 'Please enter an integer'
    # Quit the driver
    driver.quit()
