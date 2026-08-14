from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import allure
class CheckoutPage(BasePage):
        CHECKOUT_BTN = (By.ID , "checkout")
        FIRST_NAME_INPUT = (By.ID , "first-name")
        LAST_NAME_INPUT = (By.ID , "last-name")
        ZIP_CODE_INPUT = (By.ID , "postal-code")
        CONTINUE_BTN = (By.ID , "continue")
        FINISH_BTN = (By.ID , "finish")
        BACK_HOME_BTN = (By.ID , "back-to-products")
        CHECKOUT_COMPLETE_TEXT = (By.CLASS_NAME , "complete-header")

        @allure.step("Click checkout button")
        def click_checkout_button(self):
            self.click_element(self.CHECKOUT_BTN)
    
        @allure.step("Enter first name")
        def enter_first_name(self , first_name):
            self.enter_text(self.FIRST_NAME_INPUT , first_name)
    
        @allure.step("Enter last name")
        def enter_last_name(self , last_name):
            self.enter_text(self.LAST_NAME_INPUT , last_name)
    
        @allure.step("Enter zip code")
        def enter_zip_code(self , zip_code):
            self.enter_text(self.ZIP_CODE_INPUT , zip_code)
    
        @allure.step("Click continue button")
        def click_continue_button(self):
            self.click_element(self.CONTINUE_BTN)
    
        @allure.step("Click finish button")
        def click_finish_button(self):
            self.click_element(self.FINISH_BTN)
    
        @allure.step("Click back home button")
        def click_back_home_button(self):
            self.click_element(self.BACK_HOME_BTN)