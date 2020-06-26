import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class Hello_world(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'../chromedriver')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(5)

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(list(banners)))

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector('div.header-minicart span.icon')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports',
            report_name='hello-world-report'
        )
    )