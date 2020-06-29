import csv, unittest 
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class SearchDDT(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'../chromedriver')
        self.driver.get('https://www.mercadolibre.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_search_dtt(self):
        driver = self.driver

        driver.find_element_by_id('CO').click()
        search_bar = driver.find_element_by_name('as_word')
        search_bar.clear()
        search_bar.send_keys('PlayStation 4')
        search_bar.submit()

        driver.find_element_by_xpath('//*[@id="id_state"]/dd[1]/a/span[1]').click()
        driver.find_element_by_xpath('//*[@id="id_ITEM_CONDITION"]/dd[1]/a/span[1]').click()

        driver.find_element_by_class_name('ui-dropdown__link').click()
        driver.find_element_by_xpath('//*[@id="inner-main"]/aside/section[2]/dl/div/div/div/div/ul/li[3]/a').click()

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i+1}]/div/div[2]/div/h2/a/span').text
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i+1}]/div/div[2]/div/div[1]/div/span[2]').text
            prices.append(article_price)

        print(articles, prices)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)