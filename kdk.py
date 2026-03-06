import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

for book in soup.find_all("h3"):
    print(book.text)