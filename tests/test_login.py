import allure
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import pytest
from config.config import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
@allure.epic("saucelabs")
@allure.feature("Login Functionality")
@pytest.mark.parametrize("username , password", [
    ("standard_user" , "secret_sauce"),
    ("problem_user" ,"secret_sauce"),
    ("performance_glitch_user" , "secret_sauce"),
    ("error_user" , "secret_sauce"),
    ("visual_user" , "secret_sauce")
])
@allure.title("Test Valid Login")
@pytest.mark.validlogin
def test_valid_login(driver , username , password):
    with allure.step(f"Testing login for user: {username} with password: {password}"):
        driver.get(BASE_URL)
        loginpage = LoginPage(driver)
        loginpage.Login(username , password)
    assert loginpage.is_element_displayed((By.CLASS_NAME, "app_logo")) , "Login failed for user: {}".format(username)
@pytest.mark.authentication
@allure.story("invalid login")
@allure.title("invalid login")
@pytest.mark.parametrize("username , password , expexted_output", [
    ("invalid_user" , "invalid_password" , "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user" , "invalid_password", "Epic sadface: Username and password do not match any user in this service"),
    ("invalid_user" , "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
    ("" , "", "Epic sadface: Username is required"),
    ("standard_user" , "", "Epic sadface: Password is required")
])
def test_invalid_login(driver , username , password , expexted_output):
    driver.get(BASE_URL)
    loginpage = LoginPage(driver)
    loginpage.Login(username , password)
    error_message = loginpage.get_error_message()
    with allure.step(f"Testing invalid login for user: {username} with password: {password}"):
        allure.attach(f"Attempted login with username: {username} and password: {password}. Error message received: {error_message}", name="Login Attempt", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Expected error message: {expexted_output}", name="Expected Output", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Actual error message: {error_message}", name="Actual Output", attachment_type=allure.attachment_type.TEXT)
    assert error_message == expexted_output
@pytest.mark.test
@allure.story("Authentication Required")
@allure.title("Test Authentication Required")
@pytest.mark.authentication
def test_authentication_required(driver):
    with allure.step("Testing access to protected page without authentication"):
        driver.get("https://www.saucedemo.com/inventory.html")
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL)
        )
        allure.attach(f"Attempted to access protected page without authentication. Current URL: {driver.current_url}", name="Access Attempt", attachment_type=allure.attachment_type.TEXT)
    assert driver.current_url == BASE_URL , "User is not redirected to login page when accessing a protected page without authentication"
@pytest.mark.lockedout
@allure.story("Locked Out User")
@allure.title("Test Locked Out User")
@pytest.mark.authentication
def test_locked_out_user(driver):
    with allure.step("Testing login for locked out user"):
        driver.get(BASE_URL)
        loginpage = LoginPage(driver)
        loginpage.Login("locked_out_user" , "secret_sauce")
        error_message = loginpage.get_error_message()
        allure.attach(f"Attempted login with locked out user. Error message received: {error_message}", name="Login Attempt", attachment_type=allure.attachment_type.TEXT)
    assert error_message == "Epic sadface: Sorry, this user has been locked out."
    
    