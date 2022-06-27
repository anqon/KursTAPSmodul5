import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://simpletestsite.fabrykatestow.pl/'
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()


    def test1(self):
        self.driver.find_element(By.ID, "checkbox-header").click()
        self.checkbox2 = '//*[@id="checkboxes"]/input[2]'
        self.driver.find_element(By.XPATH, self.checkbox2).click()
        self.driver.get_screenshot_as_file("screenshot.png")


