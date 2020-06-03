from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://google.com')
driver.find_element_by_name('q').send_keys('Hello world' + Keys.ENTER)
driver.find_element_by_partial_link_text('Imágenes').click()
driver.find_element_by_css_selector('#islrg > div.islrc > div:nth-child(1) > a.wXeWr.islib.nfEiy.mM5pbd > div.bRMDJf.islir').click()