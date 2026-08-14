import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait 
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()
    
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    def is_element_displayed(self, locator):
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False
        
    def find_elements(self , locater):
        return self.wait.until(EC.presence_of_all_elements_located(locater))
        