from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from utils.logger import get_logger
import time
import allure
logger = get_logger(__name__)

class CatalogPage(BasePage):
    PRODUCT_IMAGES = (By.TAG_NAME , "img")
    PRODUCT_DETAILED_IMAGES = (By.CLASS_NAME , "inventory_details_img")
    PRODUCT_DETAILED_NAMES = (By.CLASS_NAME , "inventory_details_name")
    PRODUCT_TITLES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCTS = (By.CLASS_NAME , "inventory_item")
    PRODUCT_DESCRIPTIONS = (By.CLASS_NAME, "inventory_item_desc")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    INVENTORY_DEATAILS_PRICES = (By.CLASS_NAME, "inventory_details_price")

    def get_all_products(self):
        return self.find_elements(self.PRODUCTS)
    @allure.step("Get product image source")
    def get_image_src(self , product):
        image = product.find_element(*self.PRODUCT_IMAGES)
        img_src = image.get_attribute("src")
        return img_src
    @allure.step("Get product cart image source")
    def get_cart_image_src(self , product):
        product.find_element(*self.PRODUCT_IMAGES).click()
        src = self.find_element(self.PRODUCT_DETAILED_IMAGES).get_attribute("src")
        return src
    @allure.step("Get product description")
    def get_product_name(self , product):
        name = product.find_element(*self.PRODUCT_TITLES).text
        return name
    @allure.step("Get product name on detail page")
    def get_product_name_on_detail_page(self , product):
        product.find_element(*self.PRODUCT_IMAGES).click()
        name = self.find_element(self.PRODUCT_DETAILED_NAMES).text
        return name
    @allure.step("get product price in catalog page")
    def get_product_price(self , product):
        price = product.find_element(*self.PRODUCT_PRICES).text
        return price
    @allure.step("get product description in catalog page")
    def get_product_description(self , product):
        description = product.find_element(*self.PRODUCT_DESCRIPTIONS).text
        return description
    @allure.step("get product description in detail page")
    def get_product_description_on_detail_page(self , product):
        product.find_element(*self.PRODUCT_IMAGES).click()
        description = self.find_element(self.PRODUCT_DESCRIPTIONS).text
        return description
    @allure.step("get product price in detail page")
    def get_product_price_on_detail_page(self , product):
        product.find_element(*self.PRODUCT_IMAGES).click()
        price = self.find_element(self.INVENTORY_DEATAILS_PRICES).text
        return price
    
        
    