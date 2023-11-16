# This file includes methods that will parse
# the data we need from each deal box
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time


class BookingReport:
    def __init__(self, hotel_boxes):
        self.hotel_boxes = hotel_boxes

    def pull_deal_box_attributes(self):
        collection = []
        for hotel_box in self.hotel_boxes:
            # pulling hotel names
            time.sleep(3)
            hotel_name_element = hotel_box.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]')
            hotel_name = hotel_name_element.get_attribute('innerHTML').strip()
            price_element = hotel_box.find_element(By.CSS_SELECTOR, 'span[class="f6431b446c fbfd7c1165 e84eb96b1f"]')
            hotel_price = price_element.get_attribute('innerHTML').strip()
            # hotel_score_element = WebDriver.find_element(By.CSS_SELECTOR, 'div[class="d86cee9b25"]')
            # hotel_score = hotel_score_element.get_attribute('innerHTML').strip()
            collection.append(
                [hotel_name, hotel_price, ]
            )
        return collection
