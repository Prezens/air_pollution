import unittest
from selenium import webdriver


class AirKaz(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search(self):
        driver = self.driver
        driver.get('https://airkaz.org/bishkek.php')
        flags = driver.find_elements_by_tag_name('script')
        # elements = driver.find_elements_by_class_name('info-window')
        print(flags)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

