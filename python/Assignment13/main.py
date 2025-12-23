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
BLOG_TEXT = "This is an automated blog post using Selenium. #Automation #Selenium #Python"

if not FB_EMAIL or not FB_PASSWORD:
    raise ValueError("❌ Facebook credentials not set in environment variables.")

# Utility: Wait for user to press 'N' before continuing
def wait_for_next_step(step_name):
    print(f"\n➡️ STEP: {step_name}")
    while True:
        user_input = input("Press 'N' to continue to the next step... ").strip().lower()
        if user_input == 'n':
            break

# Setup Chrome
def setup_browser():
    wait_for_next_step("Setting up Chrome WebDriver")
    options = Options()
    options.add_argument("--start-maximized")  # Optional: starts browser maximized
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Login to Facebook
def login(driver):
    wait_for_next_step("Opening Facebook Login Page")
    driver.get("https://www.facebook.com/")
    time.sleep(3)

    wait_for_next_step("Filling in credentials")
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(FB_EMAIL)

    password_input = driver.find_element(By.ID, "pass")
    password_input.send_keys(FB_PASSWORD)
    password_input.send_keys(Keys.RETURN)

    print("🔐 Logged in. Waiting for feed to load...")
    time.sleep(8)

# Post status
def post_status(driver):
    wait_for_next_step("Locating post area")
    try:
        post_area = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/span")
        post_area.click()
        time.sleep(3)

        wait_for_next_step("Moving the post box")
        post_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]")
        post_box.click()
        time.sleep(3)

        wait_for_next_step("Entering blog text")
        text_box = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/p[1]")
        text_box.click()
        active_box = driver.switch_to.active_element
        active_box.send_keys(BLOG_TEXT)
        time.sleep(2)

        wait_for_next_step("Clicking post button")
        post_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]")
        post_button.click()

        print("✅ Blog post successfully posted.")
    except Exception as e:
        print("❌ Failed to post:", e)

# Close browser
def cleanup(driver):
    wait_for_next_step("Closing browser")
    time.sleep(5)
    driver.quit()

# Run Steps
try:
    driver = setup_browser()
    login(driver)
    post_status(driver)
    cleanup(driver)
except Exception as e:
    print("❌ Unexpected error:", e)
    if 'driver' in locals():
        driver.quit()
