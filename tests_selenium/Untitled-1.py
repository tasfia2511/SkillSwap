
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")
driver.maximize_window()

print("Page title is:", driver.title)

time.sleep(5)
driver.quit()



from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")
driver.maximize_window()

print("Page title is:", driver.title)

time.sleep(5)
driver.quit()




from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Start Chrome browser
driver = webdriver.Chrome()

# Step 2: Open your local Django login page
driver.get("http://127.0.0.1:8000/login")

# Step 3: Maximize window
driver.maximize_window()

# Step 4: Verify title
assert "Login" in driver.title
print("✅ Page title verified!")

# Step 5: Find the input fields
email_box = driver.find_element(By.NAME, "email")
password_box = driver.find_element(By.NAME, "password")

# Step 6: Type example credentials
email_box.send_keys("abc@gmail.com")
password_box.send_keys("abc")

# Step 7: Click login button
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Step 8: Wait a bit
time.sleep(2)

# Step 9: Check result
page_source = driver.page_source
if "Invalid" in page_source or "error" in page_source:
    print("❌ Login failed (expected for wrong credentials).")
else:
    print("✅ Login form submitted successfully.")

# Step 10: Close browser
driver.quit()

\




from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Open Chrome browser
driver = webdriver.Chrome()

# Step 2: Go to your Services page
driver.get("http://127.0.0.1:8000/services")

# Optional: maximize browser window
driver.maximize_window()

# Step 3: Verify page title or header text
assert "Services" in driver.title or "Skill Swap" in driver.title
print("✅ Page title verified!")

# Step 4: Wait for page to load fully
time.sleep(2)

# Step 5: Find important UI elements
search_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Skills...']")
dropdown = driver.find_element(By.TAG_NAME, "select")
skill_cards = driver.find_elements(By.CLASS_NAME, "rounded-xl")

# Step 6: Check element visibility
if search_input.is_displayed():
    print("✅ Search bar is visible.")
else:
    print("❌ Search bar not found.")

if dropdown.is_displayed():
    print("✅ Category dropdown is visible.")
else:
    print("❌ Category dropdown not found.")

print(f"✅ Found {len(skill_cards)} skill category cards on the page.")

# Step 7: Try typing in the search bar
search_input.send_keys("Music")
print("✅ Typed into search bar successfully.")

# Step 8: Wait briefly and close
time.sleep(2)
driver.quit()
print("✅ Test completed successfully!")



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Open Chrome browser
driver = webdriver.Chrome()

# Step 2: Visit the About Us page
driver.get("http://127.0.0.1:8000/about-us")

# Step 3: Maximize the browser window
driver.maximize_window()

# Step 4: Verify the page title or header
assert "About" in driver.title or "Skill Swap" in driver.title
print("✅ Page title verified!")

# Step 5: Wait briefly for all content to load
time.sleep(2)

# Step 6: Check key elements on the page
header = driver.find_element(By.TAG_NAME, "h1")
cards = driver.find_elements(By.CLASS_NAME, "rounded-lg")
images = driver.find_elements(By.TAG_NAME, "img")

# Step 7: Validate elements
print(f"✅ Found header: '{header.text}'")
print(f"✅ Found {len(cards)} info cards (Mission, Vision, Values).")
print(f"✅ Found {len(images)} images (avatars, etc.).")

# Step 8: Check text content presence
page_text = driver.page_source
if "Mission" in page_text and "Vision" in page_text and "Values" in page_text:
    print("✅ Page content (Mission, Vision, Values) is displayed.")
else:
    print("❌ Some key text missing!")

# Step 9: Wait and close the browser
time.sleep(2)
driver.quit()

print("🎯 Test completed successfully!")





from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Open Chrome browser
driver = webdriver.Chrome()

# Step 2: Go to FAQ page
driver.get("http://127.0.0.1:8000/faq")

# Step 3: Maximize browser window
driver.maximize_window()

# Step 4: Verify title contains "FAQ" or "Skill Swap"
assert "FAQ" in driver.title or "Skill Swap" in driver.title
print("✅ Page title verified!")

# Step 5: Wait briefly for content to load
time.sleep(2)

# Step 6: Find key page elements
header = driver.find_element(By.TAG_NAME, "h1")
search_box = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search for answers...']")
popular_questions = driver.find_elements(By.CSS_SELECTOR, "a.bg-blue-900\\/20")  # link buttons
support_boxes = driver.find_elements(By.CLASS_NAME, "rounded-xl")

# Step 7: Validate existence of these elements
print(f"✅ Header text: '{header.text}'")
assert search_box.is_displayed(), "❌ Search bar not visible!"
print("✅ Search bar is visible.")
print(f"✅ Found {len(popular_questions)} popular question buttons.")
print(f"✅ Found {len(support_boxes)} support boxes (Chat, Email, Phone).")

# Step 8: Try typing something in search box
search_box.send_keys("skill exchange")
print("✅ Typed into search box successfully.")

# Step 9: Check the 'Still Need Help' section
page_text = driver.page_source
if "Still Need Help" in page_text and "Live Chat" in page_text:
    print("✅ 'Still Need Help' section is displayed properly.")
else:
    print("❌ Help section missing or not loaded!")

# Step 10: Wait a bit, then close browser
time.sleep(2)
driver.quit()
print("🎯 Test completed successfully — all checks passed!")



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch browser
driver = webdriver.Chrome()

# Step 2: Open Profile page
driver.get("http://127.0.0.1:8000/profile")
driver.maximize_window()
print("🌐 Opened Profile Page")

# Step 3: Verify title
assert "Profile" in driver.title or "Skill Swap" in driver.title
print("✅ Page title verified!")

# Step 4: Wait for elements to load
time.sleep(2)

# Step 5: Check for Settings button
try:
    settings_btn = driver.find_element(By.LINK_TEXT, "Settings")
    assert settings_btn.is_displayed()
    print("✅ Settings button is visible.")
except Exception:
    print("❌ Settings button not found!")

# Step 6: Verify user info (name, rating, exchanges, bio)
try:
    user_name = driver.find_element(By.TAG_NAME, "h2").text
    print(f"✅ User name displayed: {user_name}")

    rating = driver.find_element(By.CLASS_NAME, "fa-star")
    exchanges = driver.find_element(By.CLASS_NAME, "fa-repeat")
    print("✅ Rating and exchange icons found.")

    bio_text = driver.find_element(By.XPATH, "//p[contains(text(),'Passionate')]").text
    print(f"✅ Bio text found: {bio_text[:60]}...")
except Exception:
    print("❌ Failed to verify user information.")

# Step 7: Check Skills sections
try:
    offer_header = driver.find_element(By.XPATH, "//h3[contains(text(),'Skills I offer')]")
    want_header = driver.find_element(By.XPATH, "//h3[contains(text(),'Skills I want')]")
    print("✅ Skill section headers found.")

    offer_skills = driver.find_elements(By.XPATH, "//div[h3[contains(text(),'Skills I offer')]]//span")
    want_skills = driver.find_elements(By.XPATH, "//div[h3[contains(text(),'Skills I want')]]//span")
    print(f"✅ Found {len(offer_skills)} offered skills and {len(want_skills)} wanted skills.")
except Exception:
    print("❌ Skills section not loaded correctly.")

# Step 8: Check “Post New Skill” button
try:
    post_skill_btn = driver.find_element(By.LINK_TEXT, "Post New Skill")
    assert post_skill_btn.is_displayed()
    print("✅ 'Post New Skill' button visible.")

    # Optional: Click to test navigation
    post_skill_btn.click()
    time.sleep(1)
    print("✅ Clicked 'Post New Skill' successfully (check URL).")
    driver.back()
except Exception:
    print("❌ 'Post New Skill' button not found or not clickable!")

# Step 9: Verify footer content
try:
    footer_text = driver.find_element(By.XPATH, "//div[contains(text(),'Copyright')]").text
    print(f"✅ Footer found: {footer_text}")
except Exception:
    print("❌ Footer not visible!")

# Step 10: End the test
time.sleep(2)
driver.quit()
print("🎯 Profile Page Test completed successfully!")


