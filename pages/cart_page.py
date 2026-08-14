from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from utils.logger import get_logger
from selenium.common.exceptions import NoSuchElementException , TimeoutException
import time
import allure
logger = get_logger(__name__)
class CartPage(BasePage):
    ADD_TO_CART_BTN = (By.XPATH , ".//button[text()='Add to cart']")
    REMOVE_BTN = (By.XPATH , ".//button[text()='Remove']")
    CART_BTN = (By.CLASS_NAME , "shopping_cart_link")
    PRODUCT_NAMES = (By.CLASS_NAME , "inventory_item_name")
    ADD_BTN_CLASS = (By.CLASS_NAME , "btn_primary")
    REMOVE_BTN_CLASS = (By.CLASS_NAME , "btn_secondary")
    
    def add_to_cart(self , product):
        product.find_element(*self.ADD_TO_CART_BTN).click()
    
    def remove_from_cart(self , product):
        try:
            product.find_element(*self.REMOVE_BTN).click()
        except(NoSuchElementException , TimeoutException):
            pass
    
    def check_cart_products(self):
        self.find_element(self.CART_BTN).click()
        elements =  self.find_elements(self.PRODUCT_NAMES)
        productsInCart = [element.text for element in elements]
        logger.info(productsInCart)
        return productsInCart
    def remove_all_elements_from_cart(self):
        while True:
            btns = btns = self.driver.find_elements(*self.REMOVE_BTN_CLASS)
            if not btns:
                break

            btns[0].click()