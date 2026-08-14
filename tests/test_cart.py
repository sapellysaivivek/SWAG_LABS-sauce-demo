import pytest
import allure
from config.config import BASE_URL
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage
from fixture.driver_factory import get_driver
from utils.logger import get_logger
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
logger = get_logger(__name__)
@pytest.mark.cart
@allure.feature("CART")
@allure.story("verifying adding and removing from cart")
@allure.title("Verifying Adding of products in cart is consistent for all users")
@allure.description("Adding the products in cart and verifying the cart for respective changes ")
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
])
def test_add_to_cart(driver, username , password):
    driver.get(BASE_URL)
    loginpage = LoginPage(driver)
    loginpage.Login(username , password)
    catalogpage = CatalogPage(driver)
    products = catalogpage.get_all_products()
    nameOfProduct = catalogpage.get_product_name(products[1])
    for i, product in enumerate(products):
        print(i, catalogpage.get_product_name(product))
    cartPage = CartPage(driver)
    cartPage.add_to_cart(products[1])
    all_cart_products = cartPage.check_cart_products()
    assert nameOfProduct in all_cart_products
    driver.back()
    products = catalogpage.get_all_products()
    cartPage.remove_from_cart(products[1])
@pytest.mark.cart1
@allure.feature("CART")
@allure.story("verifying user Isolation")
@allure.title("Verifying user carts are exclusive")
@allure.description("products added or removed in one user's cart  shouldn't appear in anothers cart")
@pytest.mark.parametrize("username, password", [
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
])    
def test_user_isolation(driver , username , password):
    driver.get(BASE_URL)
    loginpage = LoginPage(driver)
    loginpage.Login("standard_user" , "secret_sauce")
    catalogpage = CatalogPage(driver)
    cartPage = CartPage(driver)
    with allure.step("removing all products froom cart"):
        cartPage.remove_all_elements_from_cart()
    with allure.step("add 2, 4, 6th product to the cart"):
        products = catalogpage.get_all_products()
        cartPage.add_to_cart(products[1])
        cartPage.add_to_cart(products[3])
        cartPage.add_to_cart(products[5])
        names = cartPage.check_cart_products()
        allure.attach(f"Products added to cart for standard_user: {names}", name="Cart Products", attachment_type=allure.attachment_type.TEXT)
        loginpage.logout()
        
    with allure.step("verifying the products are not the same in carts of other users"):
        loginpage.Login(username , password)
        products_in_cart = cartPage.check_cart_products()
        allure.attach(f"Products in cart for {username}: {products_in_cart}", name="Cart Products", attachment_type=allure.attachment_type.TEXT)
        assert names != products_in_cart
            