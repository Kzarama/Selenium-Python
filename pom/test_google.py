import csv, unittest 
from selenium import webdriver
from google_page import GooglePage

class SearchDDT(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r'../chromedriver')

    def test_search_dtt(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Github')

        self.assertEquals('Github', google.keyword)

    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)