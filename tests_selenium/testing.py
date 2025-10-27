from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start the browser (Make sure you have ChromeDriver or EdgeDriver installed)
driver = webdriver.Chrome()

try:
    # Open your Django home page
    driver.get("http://127.0.0.1:8000/")
    driver.maximize_window()

    # Wait for elements to load
    time.sleep(2)

    # ✅ Check page title
    assert "Skill Swap" in driver.title
    print("✅ Page title contains 'Skill Swap'")

    # ✅ Check Hero section heading
    hero_heading = driver.find_element(By.TAG_NAME, "h1").text
    assert "SkillSwap" in hero_heading
    print("✅ Found hero heading")

    # ✅ Check buttons
    explore_button = driver.find_element(By.LINK_TEXT, "Explore & Learn >")
    teach_button = driver.find_element(By.LINK_TEXT, "Share Your Skill >")
    print("✅ Buttons found successfully")

    # ✅ Check footer contact info
    footer_email = driver.find_element(By.XPATH, "//*[contains(text(),'skillswap@gmail.com')]")
    print("✅ Footer contact found")

    print("🎉 All tests passed successfully!")

finally:
    # Close the browser after 3 seconds
    time.sleep(3)
    driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver (make sure ChromeDriver is installed)
driver = webdriver.Chrome()

try:
    # Step 1: Open the How It Works page
    driver.get("http://127.0.0.1:8000/how-it-works/")
    driver.maximize_window()
    time.sleep(2)  # wait for page to load

    # ✅ Check page title
    assert "How It Works" in driver.title
    print("✅ Page title verified")

    # ✅ Check main heading
    heading = driver.find_element(By.TAG_NAME, "h1").text
    assert "Learning has never been easier" in heading
    print("✅ Main heading found")

    # ✅ Check 'Start Your Journey' button
    button = driver.find_element(By.LINK_TEXT, "Start Your Journey >")
    assert button.is_displayed()
    print("✅ 'Start Your Journey' button is visible")

    # ✅ Check Step 1, Step 2, Step 3
    steps = driver.find_elements(By.CLASS_NAME, "text-lg")
    step_titles = [s.text for s in steps]
    assert "Create Profile" in step_titles
    assert "Get Matched" in step_titles
    assert "Learn Together" in step_titles
    print("✅ All 3 steps are present")

    print("🎉 All tests passed successfully!")

finally:
    # Close browser after a short delay
    time.sleep(3)
    driver.quit()

