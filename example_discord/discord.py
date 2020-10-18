from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# driver
driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://discord.com/login')
driver.implicitly_wait(10)

# username
username = driver.find_element_by_xpath(
    '/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input')
username.send_keys('USERNAME')
# password
password = driver.find_element_by_xpath(
    '/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
password.send_keys('PASSWORD')
# login button
driver.find_element_by_xpath(
    '/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]').click()

driver.implicitly_wait(20)
# server
driver.find_element_by_xpath(
    'SERVER').click()
# channel
driver.find_element_by_xpath(
    'CHANNEL').click()
# input message
input_message = driver.find_element_by_xpath(
    '/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')

while True:
    # write message
    input_message.send_keys('owo hunt')
    # press enter
    input_message.send_keys(Keys.ENTER)
    # wait
    time.sleep(random.randint(16, 60))
