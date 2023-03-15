import sys
import time
from io import StringIO

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_healthforce_hyperlink():
    driver = webdriver.Chrome()
    time.sleep(2)
    driver.get("http://localhost:6464/")
    driver.implicitly_wait(15)
    driver.find_element(By.LINK_TEXT, 'Healthforce').is_displayed()
    time.sleep(2)
    driver.quit()
