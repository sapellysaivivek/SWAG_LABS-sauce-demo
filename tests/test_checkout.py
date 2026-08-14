from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import allure
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
from config.config import BASE_URL
from pages.checkooutpage import CheckoutPage
import pytest
@allure.feature("Checkout Process")
@allure.step("Test Checkout Process")
@allure.title("Test Checkout Process")
@allure.description("This test verifies the checkout process for different users.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.checkout
@pytest.mark.parametrize("username, password", 
                [("problem_user", "secret_sauce"),
                ("performance_glitch_user", "secret_sauce"),
                ("error_user", "secret_sauce"),
                ("visual_user", "secret_sauce"),
                ("standard_user", "secret_sauce")])                                                
def test_checkout_process(driver , username , password):
    driver.get(BASE_URL)
    loginpage = LoginPage(driver)
    loginpage.Login(username, password)
    catalogpage = CatalogPage(driver)
    products = catalogpage.get_all_products()
    cartpage = CartPage(driver)
    with allure.step("Adding first product to cart"):
        cartpage.add_to_cart(products[0])
    with allure.step("Proceeding to checkout"):
        cartpage.find_element(cartpage.CART_BTN).click()
        checkout_button = cartpage.find_element((By.ID, "checkout"))
        checkout_button.click()
    with allure.step("Filling in checkout information"):
        checkoutpage = CheckoutPage(driver)
        checkoutpage.enter_first_name("John")
        checkoutpage.enter_last_name("Doe")
        checkoutpage.enter_zip_code("12345")
    with allure.step("Continuing to the next step of checkout"):
        checkoutpage.click_continue_button()
    with allure.step("Finishing the checkout process"):
        checkoutpage.click_finish_button()
        
    
    