import sys
from io import StringIO

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_with_only_spaces():
    # initialising chrome
    driver = webdriver.Chrome()
    # calling url required
    driver.get("http://localhost:6464/")
    assert "The greatest factorial calculator!" in driver.title
    driver.find_element(By.CSS_SELECTOR, '#number').send_keys('      ')
    driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
    sys.stdout = buffer = StringIO()
    # Quit the driver
    driver.quit()