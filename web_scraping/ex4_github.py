from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Set up Chrome WebDriver
driver = webdriver.Chrome(service=Service())


# Step 4: Enter credentials (replace with your actual credentials)
username = "demo_user"  # Your GitHub username here
password = "secret_pass"    # Your GitHub password here

# Navigate to the SeleniumBase demo login page
driver.get("https://seleniumbase.io/simple/login")

# Locate the username field and enter the username
username_field = driver.find_element(By.CSS_SELECTOR, "#username")
username_field.send_keys(username)

# Locate the password field and enter the password
password_field = driver.find_element(By.CSS_SELECTOR, "#password")
password_field.send_keys(password)

# Click the login button
login_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign in')]")
login_button.click()

# Wait for a few seconds to allow the page to load
time.sleep(5)

# Check if login was successful by looking for a welcome message or specific element
if "Welcome!" in driver.page_source:
    print("Login successful!")
else:
    print("Login failed!")

# Step 2: Navigate to GitHub login page
url = 'https://github.com/login'
driver.get(url)

# Allow some time for the page to load
time.sleep(2)

# Step 3: Locate username and password fields
username_field = driver.find_element(By.ID, 'login_field')
password_field = driver.find_element(By.ID, 'password')

# Step 4: Enter credentials (replace with your actual credentials)
username = "# Your GitHub username here"  # Your GitHub username here
password = "# Your GitHub password here"    # Your GitHub password here

username_field.send_keys(username)  # Enter username
password_field.send_keys(password)    # Enter password

# Step 5: Submit the login form
password_field.send_keys(Keys.RETURN)  # Submit the form by pressing Enter

# Allow some time for the login process to complete
time.sleep(10)

# Step 6: Verify login success by checking for a specific element on the dashboard page 
try:
    driver.find_element(By.XPATH, "//summary[@aria-label='View profile and more']")
    print("Login successful!")
except Exception as e:
    print("Login failed:", e)


# Step 7: Close the browser window 
driver.quit()