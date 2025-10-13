from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def setup():
    """Initialize Chrome WebDriver and quit after test"""
    driver = webdriver.Chrome()  # Make sure chromedriver is installed and in PATH
    driver.maximize_window()
    yield driver
    driver.quit()


def test_homepage_title(setup):
    """✅ Test if homepage title contains SkillSwap"""
    driver = setup
    driver.get("http://127.0.0.1:8000/")

    title = driver.title.lower()
    assert "skill" in title and "swap" in title, f"❌ Unexpected homepage title: {title}"


def test_login_page(setup):
    """✅ Test login form works correctly"""
    driver = setup
    driver.get("http://127.0.0.1:8000/login")

    wait = WebDriverWait(driver, 15)  # Wait for page to load

    # Locate fields
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))

    # Enter valid credentials
    email_field.clear()
    email_field.send_keys("tasfia2511@gmail.com")  # your real account
    password_field.clear()
    password_field.send_keys("TomaTammi")          # your real password

    # Click the login button
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()

    # ✅ Wait for a post-login element instead of URL
    # Example: user menu or logout link that only appears after login
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'logout')]")))

    # Optional: assert URL contains dashboard or check element text
    assert "dashboard" in driver.current_url.lower() or \
           driver.find_element(By.XPATH, "//a[contains(@href,'logout')]"), "❌ Login failed"

