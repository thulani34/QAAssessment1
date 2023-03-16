import sys
import time
import unittest
from io import StringIO

from selenium import webdriver
from selenium.webdriver.common.by import By


class Factorial(unittest.TestCase):

    def SetUp(self):
        self.driver = None
        self.driver = webdriver.Chrome()
        time.sleep(2)
        self.driver.maximize_window()
        self.driver.get("http://localhost:6464/")

    def test_factorial_of_7(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, '#number').send_keys('7')
        driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
        time.sleep(3)
        element = driver.find_element(By.XPATH, "//p[@id='resultDiv']")
        assert element.text == 'The factorial of 7 is: 5040'
        time.sleep(3)

    def test_alpha_characters(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, '#number').send_keys('7@8$%')
        driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//p[@id='resultDiv']")
        assert element.text == 'Please enter an integer'

    def test_healthforce_hyperlink(self):
        driver = self.driver
        driver.implicitly_wait(15)
        driver.find_element(By.LINK_TEXT, 'Healthforce').is_displayed()
        time.sleep(2)
        driver.quit()

    def test_integer_with_lower_boundry(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, '#number').send_keys('0007')
        driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()

    def test_integer_with_upper_boundry(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, '#number').send_keys('1')
        driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()

    def test_integer_with_leading_zeroes(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, '#number').send_keys('000000')
        driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
        time.sleep(2)

    def test_integer_with_leading_minus_sign(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, '#number').send_keys('----7')
        driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
        element = driver.find_element(By.XPATH, "//p[@id='resultDiv']")
        assert element.text == 'Please enter an integer'

    def test_integer_with_leading_plus_sign(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, '#number').send_keys('+++7')
        driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//p[@id='resultDiv']")
        assert element.text == 'Please enter an integer'

    def test_integer_with_leading_spaces(self):
        driver = self.driver
        assert "Factoriall" in driver.title
        driver.find_element(By.CSS_SELECTOR, '#number').send_keys('   7')
        driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()

    def test_number_with_decimal_point(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, '#number').send_keys('7.01')
        driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//p[@id='resultDiv']")
        assert element.text == 'Please enter an integer'

    def test_privacy_hyperlink(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, 'Privacy').is_displayed()
        time.sleep(2)

    def test_special_character(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, '#number').send_keys('@#$%^&')
        driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
        element = driver.find_element(By.XPATH, "//p[@id='resultDiv']")
        assert element.text == 'Please enter an integer'

    def test_terms_conditions_hyperlink(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, 'Terms and Conditions').is_displayed()
        time.sleep(2)

    def test_with_nothing_entered(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, '#number').send_keys('')
        driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
        element = driver.find_element(By.XPATH, "//p[@id='resultDiv']")
        assert element.text == 'Please enter an integer'
        time.sleep(2)

    def test_with_only_spaces(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, '#number').send_keys('      ')
        driver.find_element(By.XPATH, "//button[@id='getFactorial']").click()
        element = driver.find_element(By.XPATH, "//p[@id='resultDiv']")
        assert element.text == 'Please enter an integer'
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
