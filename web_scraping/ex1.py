import requests
from bs4 import BeautifulSoup

# Target URL for scraping
url = 'http://books.toscrape.com/'
response = requests.get(url)
html_content = response.content

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract book titles
titles = soup.find_all('h3')
for title in titles:
    print(title.a['title'])  # Get the title attribute of the anchor tag