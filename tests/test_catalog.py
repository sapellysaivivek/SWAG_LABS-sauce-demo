import pytest
import allure
from config.config import BASE_URL
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage
from fixture.driver_factory import get_driver
from utils.logger import get_logger
from selenium.webdriver.common.by import By
logger = get_logger(__name__)
@allure.epic("saucelabs")
@allure.feature("Catalog Functionality")
@allure.story("Product Image and Description Verification")
@pytest.mark.catalogtest
@allure.title("Test Product Image and Description")
@allure.description("Verify that all products are available for every user")
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
])
def test_all_elements_available(driver , username , password):
    logger.critical(f"starting products availability for {username}")
    driver.get(BASE_URL)
    loginpage = LoginPage(driver)
    loginpage.Login(username , password)
    with allure.step(f"Verifying weather all products are available for {username}"):
        logger.critical(f"logged in successfully")
        catalogpage = CatalogPage(driver)
        products = catalogpage.get_all_products()
        allure.attach(driver.get_screenshot_as_png() , name = "Screenshot" , attachment_type=allure.attachment_type.PNG)
        assert isinstance(products , list) , f"the return data type is {type(products)}"
        assert len(products) == 6 , f"All the products are not available for {username}"
@pytest.mark.catalogtest
@allure.story("verifying image consistency accrose different users")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("check weather the images and descriptions are accurate")
@allure.description("Verify that the product image and description match in catalog and product detail pages for various users.")
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
])
def test_image_accuracy_for_all_users(driver , username , password):
    driver.get(BASE_URL)
    loginpage = LoginPage(driver)
    loginpage.Login(username , password)
    logger.critical(f"testing image accuracy for {username}")
    catalogpage = CatalogPage(driver)
    products = catalogpage.get_all_products()
    match = 0
    names = []
    for i in range(len(products)):
        with allure.step(f"collecting image src in catalog page {username}"):
            products = catalogpage.get_all_products()
            name = catalogpage.get_product_name(products[i])
            src =catalogpage.get_image_src(products[i])
            allure.attach(
                driver.get_screenshot_as_png() , name = f"{name}_image_on_catalog" , attachment_type = allure.attachment_type.PNG
            )
        with allure.step(f"collecting image src in details page"):
            cart_image_src = catalogpage.get_cart_image_src(products[i])
            if src == cart_image_src:
                match = match+1
            else:
                names.append(name)
            allure.attach(
                driver.get_screenshot_as_png() , name = f"{name}_image_on_catalog" , attachment_type = allure.attachment_type.PNG
            )
            driver.back()
            
    with allure.step("verifying weather all the products have accurate images"):
        assert match == len(products) , f"images for the products {names} are incorrect"
        allure.attach(body = f"{names} images are inconsistent" , attachment_type=allure.attachment_type.TEXT)   
@pytest.mark.catalogtest
@allure.story("verifying Data consistency accrose different users")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("check weather the data are accurate")
@allure.description("Verify that the product data match in catalog and product detail pages for various users.")
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
])
def test_data_consistency_in_details_page(driver , username , password):
    driver.get(BASE_URL)
    loginpage = LoginPage(driver)
    loginpage.Login(username , password)
    Catalogpage = CatalogPage(driver)
    products = Catalogpage.get_all_products()
    match = 0
    names = []  
    for i in range(len(products)):
        products = Catalogpage.get_all_products()
        with allure.step(f"collecting name in catalog page {username}"):
            products = Catalogpage.get_all_products()
            name = Catalogpage.get_product_name(products[i])
            allure.attach(
                driver.get_screenshot_as_png() , name = f"{name}_image_on_catalog" , attachment_type = allure.attachment_type.PNG
            )
        with allure.step(f"collecting name in details page"):
            cart_image_name = Catalogpage.get_product_name_on_detail_page(products[i])
            if name == cart_image_name:
                match = match+1
            else:
                names.append(name)
            allure.attach(
                f"there is data inconsistency for {names}" , name = f"{name}_image_on_catalog" , attachment_type = allure.attachment_type.PNG
            )
            driver.back()
    with allure.step("verifying weather all the products have accurate Data between catalog page and details page"):
            assert match == len(products) , f"data for the products {names} are inconsistent"
            allure.attach(body = f"{names} data are inconsistent" , attachment_type=allure.attachment_type.TEXT)   
            
@pytest.mark.catalogtest2
@allure.story("verifying Data consistency (price and description) accrose different users ")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("check weather the data are accurate")
@allure.description("Verify that the product data (price and description) match in catalog and product detail pages for various users.")
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
])
def test_data_consistency_in_details_page(driver , username , password):
    driver.get(BASE_URL)
    loginpage = LoginPage(driver)
    loginpage.Login(username , password)
    Catalogpage = CatalogPage(driver)
    products = Catalogpage.get_all_products()
    match = 0
    names = []  
    for i in range(len(products)):
        products = Catalogpage.get_all_products()
        with allure.step(f"collecting price in catalog page {username}"):
            price = Catalogpage.get_product_price(products[i])
            allure.attach(
                driver.get_screenshot_as_png() , name = f"{price}_image_on_catalog" , attachment_type = allure.attachment_type.PNG
            )
        with allure.step(f"collecting price in details page"):
            cart_image_price = Catalogpage.get_product_price_on_detail_page(products[i])
            if price == cart_image_price:
                match = match+1
            else:
                names.append(price)
            allure.attach(
                f"there is data inconsistency for {names}" , name = f"{price}_image_on_catalog" , attachment_type = allure.attachment_type.TEXT
            )
            driver.back()
    with allure.step("verifying weather all the products have accurate Data between catalog page and details page"):
            assert match == len(products) , f"data for the products {names} are inconsistent"
            allure.attach(body = f"{names} data are inconsistent" , attachment_type=allure.attachment_type.TEXT)
    

           