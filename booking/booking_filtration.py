# This file will include a class with instance methods
# that will be responsible for interacting with the website
# after we've found results, to aplly filters
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time


class Bookingfiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def star_filtration(self, *star_values):
        star_child_elements = self.driver.find_elements(By.XPATH, "//div[@class='ffb9c3d6a3 f85e2160d2'][4]//*[@class='c733693b78']")
        for star_value in star_values:
            star_child_element = self.driver.find_element(By.XPATH, f"//div[@class='ffb9c3d6a3 f85e2160d2'][4]//*[contains(text(), '{star_value} star')]")
            star_child_element.click()

    def sort_by_lowest_prices_first(self):
        time.sleep(5)
        sort_by_dropdown_element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]')
        sort_by_dropdown_element.click()
        # lowest_prices_element = self.driver.find_element(By.XPATH, './/*[contains(text(), "Price (lowest first)")]')
        lowest_prices_element = self.driver.find_element(By.XPATH, "//span[text()='Price (lowest first)']")
        lowest_prices_element.click()


