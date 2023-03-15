import sys
import time
from io import StringIO

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_integer_with_lower_boundry():
    driver = webdriver.Chrome()
    time.sleep(2)
    driver.get("http://localhost:6464/")
    driver.find_element(By.CSS_SELECTOR, '#number').send_keys('0007')
    driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
    time.sleep(2)
    driver.quit()
