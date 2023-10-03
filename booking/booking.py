import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from booking.booking_filtration import Bookingfiltration
from selenium.webdriver.support import expected_conditions as EC
import booking.constants as const
import os


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        super(Booking, self).__init__()
        self.teardown = teardown
        self.implicitly_wait(15)
        self.maximize_window()

    def keep_browser_open(self):
        while self.teardown:  # Runs the loop while teardown is True
            pass

    def landing_first_page(self):
        self.get(const.BASE_URL)

    def accept_cookies(self):
        try:
            accept_button = self.find_element(By.ID, "onetrust-accept-btn-handler")
            accept_button.click()
        except:
            pass

    def bypass_registration_prompt(self):
        try:
            close_registration_prompt = self.find_element(By.CLASS_NAME, "f4552b6561")
            close_registration_prompt.click()
        except:
            pass

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()
        selected_currency_element = self.find_element(By.XPATH,
                                                      f"//button//span[@class='cf67405157']//div[@class=' ea1163d21f'][contains(text(),"
                                                      f"'{currency}')]")
        selected_currency_element.click()

    def insert_destination(self, destination_name):
        destination_field = self.find_element(By.ID, ':re:')
        destination_field.clear()
        destination_field.send_keys(destination_name)
        time.sleep(3)
        first_result = self.find_element(By.CLASS_NAME, 'a80e7dc237')
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.XPATH, f'//td//span[@data-date="{check_in_date}"]')
        check_in_element.click()
        check_out_element = self.find_element(By.XPATH, f'//td//span[@data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count=1):
        occupancy_selection_element = self.find_element(By.XPATH, '//button[@data-testid="occupancy-config"]')
        occupancy_selection_element.click()

        while True:
            decrease_element = self.find_element(By.XPATH, "//button[@class='a83ed08757 c21c56c305 f38b6daa18 d691166b09 "
                                                         "ab98298258 deab83296e bb803d8689 e91c91fa93']//span["
                                                         "@class='fcd9eec8fb bf9a32efa5']//*[name()='svg']//*[name("
                                                         ")='path' and contains(@d,'M20.25 12.')]")
            decrease_element.click()
            #If adult value reaches 1, we should break out of the loop
            adult_count_element = self.find_element(By.CLASS_NAME, 'd723d73d5f')
            adult_count = adult_count_element.text #get the final adult count
            if int(adult_count) == 1:
                break

        # now we increase the adult count to the required number
        increase_element = self.find_element(By.CLASS_NAME, "f4d78af12a")
        for _ in range(count - 1):
            increase_element.click()

    def click_search(self):
        search_element = self.find_element(By.CLASS_NAME, 'aa11d0d5cd')
        search_element.click()

    def change_language(self):
        """Changes language to english"""
        language_choice_element = self.find_element(By.CLASS_NAME, 'ed3971de08')
        language_choice_element.click()
        english_element = self.find_element(By.XPATH, "//div[@data-testid='Рекомендовано для вас']//span[@class='cf67405157'][normalize-space()='English (UK)']")
        english_element.click()


    def apply_filtration(self):
        filtration = Bookingfiltration(driver=self)
        filtration.star_filtration()


