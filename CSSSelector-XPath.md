Write a locator (CSS selector/XPath) for the red form validation styling
------------------------------------------------------------------------
driver.find_element(By.CSS_SELECTOR, '#number').send_keys('7')
driver.find_element(By.XPATH, "//input[@id='number']")
