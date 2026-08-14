from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import allure
class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder = 'Username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder = 'Password']")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
    OPEN_BTN = (By.XPATH, "//button[text()='Open Menu']")
    LOGOUT = (By.XPATH, "//a[@id='logout_sidebar_link']")
    
    @allure.step("Enter username")
    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)
    @allure.step("Click login button")
    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)
    @allure.step("Get error message")
    def get_error_message(self):
        return self.get_element_text(self.ERROR_MESSAGE)
    @allure.step("Perform login")
    def Login(self , username , password ):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        with allure.step("Login Attempt"):
            allure.attach(f"Attempting to login with username: {username} and password: {password}", attachment_type=allure.attachment_type.TEXT)
    @allure.step("Logout")
    
    def logout(self):
        self.click_element(self.OPEN_BTN)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT)
        ).click()
        
