from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Step 1: Set up Chrome WebDriver
driver = webdriver.Chrome()

# Step 2: Navigate to Hacker News
url = 'https://news.ycombinator.com/'
driver.get(url)

# Allow some time for the page to load
time.sleep(2)

# Step 3: Scrape titles and links
stories = driver.find_elements(By.CLASS_NAME, 'titleline')
print(stories)

for story in stories:
    title = story.text  # Get the title text
    print(f'Title: {title}\n')

# Step 4: Close the browser
driver.quit()