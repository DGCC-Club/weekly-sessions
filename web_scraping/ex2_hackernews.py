import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = 'https://news.ycombinator.com/'
response = requests.get(url)
html_content = response.content

# Step 2: Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Extract data
stories = soup.find_all('tr', class_='athing')  # Each story is in a <tr> with class 'athing'

for story in stories:
    title = story.find_all('td')[2].get_text()  # Extract title text
    print(f'Title: {title}')