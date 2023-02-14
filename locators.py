from selenium.webdriver.common.by import By


BASE_URL = 'https://www.booking.com/'
CURRENCY = (By.XPATH, '//div[@class="a1b3f50dcd b2fe1a41c3 a1f3ecff04 db7f07f643 c7b46bab72"]/span[@class="cb5ebe3ffb"][1]/button[@class="fc63351294 a822bdf511 e3c025e003 cfb238afa1 e634344169"]')
CHOOSE_CURRENCY = (By.XPATH, '//button[@class="bui-button bui-button--light bui-button--large"]/span[@class="bui-button__text"]/span[aria-hidden="true"]')
# button[data-modal-aria-label="Select your currency"]
