from selenium import webdriver
from selenium.webdriver.common.by import By
import Booking.locators as locators
from Booking.booking_filtration import BookingFiltration
import time


class BookingPage(webdriver.Firefox):
    def __init__(self):
        super(BookingPage, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()
        print('exit')

    def open_first_page(self):
        self.get(locators.BASE_URL)

    def change_currency(self):
        self.find_element(By.XPATH, '//div[@class="a1b3f50dcd b2fe1a41c3 a1f3ecff04 db7f07f643 c7b46bab72"]/span[@class="cb5ebe3ffb"][1]').click()
        button = self.find_element(By.XPATH, '//div[text()="USD"]')
        self.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    def change_language(self, language='English (US)'):
        self.find_element(By.CSS_SELECTOR, '[data-testid="header-language-picker-trigger"]').click()
        lang = self.find_element(By.XPATH, f'//span[text()="{language}"]')
        self.execute_script("return arguments[0].scrollIntoView(true);", lang)
        lang.click()

    def close_button(self):
        self.find_element(By.ID, 'close').click()

    def choose_direction(self, city):
        direction = self.find_element(By.ID, 'ss')
        direction.clear()
        direction.send_keys(f'{city}')
        self.find_element(By.CSS_SELECTOR, '[data-i="0"]').click()

    def select_data(self, check_in, check_out):
        self.find_element(By.CSS_SELECTOR, f'[data-date="{check_in}"]').click()
        self.find_element(By.CSS_SELECTOR, f'[data-date="{check_out}"]').click()

    def select_adults(self, count=1):
        button = self.find_element(By.ID, 'xp__guests__toggle')
        button.click()

        while True:
            decrease_button = self.find_element(By.CSS_SELECTOR, '[aria-label="Decrease number of Adults"]')
            decrease_button.click()
            adult_value = self.find_element(By.ID, 'group_adults').get_attribute('value')
            if int(adult_value) == 1:
                break

        increase_button = self.find_element(By.CSS_SELECTOR, '[aria-label="Increase number of Adults"]')
        for i in range(count-1):
            increase_button.click()

    def search_click(self):
        button = self.find_element(By.CLASS_NAME, 'sb-searchbox__button ')
        self.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    def filters(self):
        filtration = BookingFiltration(driver=self)
        filtration.stars(4, 5)














