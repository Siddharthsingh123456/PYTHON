import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

FB_EMAIL = os.getenv("FB_EMAIL")
FB_PASSWORD = os.getenv("FB_PASSWORD")
BLOG_TEXT = "This is an automated blog post using Selenium.#Automation #Selenium #Python"

if not FB_EMAIL or not FB_PASSWORD:
    raise ValueError("❌ Facebook credentials not set in environment variables.")

# Setup Chrome
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open Facebook
driver.get("https://www.facebook.com/")
time.sleep(3)

# Login
email_input = driver.find_element(By.ID, "email")
email_input.send_keys(FB_EMAIL)

password_input = driver.find_element(By.ID, "pass")
password_input.send_keys(FB_PASSWORD)
password_input.send_keys(Keys.RETURN)

print("🔐 Logged in. Waiting for feed to load...")
time.sleep(8)  # wait for feed to load

# Post status
try:
    post_area = driver.find_element(By.XPATH, "//span[text()=\"What's on your mind?\"]")
    post_area.click()
    time.sleep(3)

    active_box = driver.switch_to.active_element
    active_box.send_keys(BLOG_TEXT)
    time.sleep(2)

    post_button = driver.find_element(By.XPATH, "//div[@aria-label='Post']")
    post_button.click()

    print("✅ Blog post successfully posted.")
except Exception as e:
    print("❌ Failed to post:", e)

# Close browser
time.sleep(5)
driver.quit()
