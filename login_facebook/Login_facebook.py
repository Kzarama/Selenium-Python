from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# log in
driver.get('https://www.facebook.com/')
driver.find_element_by_id('email').send_keys('EMAIL')
driver.find_element_by_id('pass').send_keys('PASSWORD')
driver.find_element_by_id('u_0_b').click()