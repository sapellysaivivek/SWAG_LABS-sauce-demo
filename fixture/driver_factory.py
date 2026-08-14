from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from config.config import execution_mode


def get_driver(browser):

    if execution_mode == "local":

        options = webdriver.ChromeOptions()

        options.add_argument("--start-maximized")
        
        options.add_argument("--headed")  # Use new headless mode for Chrome
        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_leak_detection_enabled": False,
                "profile.password_manager_leak_detection": False
            }
        )

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

        return driver

    # =========================
    # REMOTE EXECUTION
    # =========================

    if browser == "chrome":

        options = webdriver.ChromeOptions()

        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-notifications")

        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_leak_detection_enabled": False
            }
        )

    elif browser == "edge":

        options = webdriver.EdgeOptions()

        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-notifications")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }
        )

    elif browser == "firefox":

        options = webdriver.FirefoxOptions()

        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        # Firefox does NOT use add_experimental_option()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=options
    )

    return driver