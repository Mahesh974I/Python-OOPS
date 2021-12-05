### Importing required packages 
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

## Initialisinsg browser
class Testing():
    driver = webdriver.Firefox()
    def __init__(self,driver = driver):
        self.driver= driver
    def test(self):
        self.driver.get('https://www.google.com')
        self.driver.find_element_by_name('q').send_keys('python automation ')
        self.driver.find_element_by_name('btnK').send_keys(Keys.ENTER)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.quit()
        print('test completed successful')

# if __name__ == '__main':
b = Testing()
b.test()