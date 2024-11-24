import requests
from bs4 import BeautifulSoup

for i in range(1, 51):
    response = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
    response.encoding = 'UTF-8'
    soup = BeautifulSoup(response.text, features="html.parser")

    books = soup.find_all("article", {"class": "product_pod"})
    for book in books:
        title = book.h3.a['title']
        price = book.find("p", {"class": "price_color"}).text
        print(f"{title}: {price}")
