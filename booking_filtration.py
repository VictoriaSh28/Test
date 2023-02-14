from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def stars(self, *star_values):
        stars_box = self.driver.find_element(By.ID, 'filter_group_class_:R1kq:')
        stars_box_child = stars_box.find_elements(By.CSS_SELECTOR, '*')

        for star_value in star_values:
            for star in stars_box_child:
                if str(star.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star.click()

