import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_alpha_characters():
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(2)
    driver.get("http://localhost:6464/")
    print(driver.title)
    driver.implicitly_wait(15)
    driver.find_element(By.CSS_SELECTOR, '#number').send_keys('7@8$%')
    driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
    time.sleep(2)
    element = driver.find_element(By.XPATH, "//p[@id='resultDiv']")
    assert element.text == 'Please enter an integer'
    time.sleep(2)
    driver.quit()
