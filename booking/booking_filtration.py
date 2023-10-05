# This file will include a class with instance methods
# that will be responsible for interacting with the website
# after we've found results, to aplly filters
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Bookingfiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def star_filtration(self):
        star_child_elements = self.driver.find_elements(By.XPATH, "//div[@class='ffb9c3d6a3 f85e2160d2'][4]//*[@class='c733693b78']")
        print(len(star_child_elements))
