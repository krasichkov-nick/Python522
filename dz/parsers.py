from bs4 import BeautifulSoup
import requests


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        news = self.html.find_all("div", class_="catalog__product-grid catalog__product")
        for item in news:
            title = item.find("div", class_="product-item__link product-item-grid__link").text
            href = item.find("div", class_="product-item__link product-item-grid__link").find("a")["href"]
            price = item.find("div", class_="product-item-price").text.strip()
            self.res.append({
                'title': title,
                'href': href,
                'price': price
            })
            # print(self.res)

    def save(self):
        with open(self.path, 'w', encoding="utf-8") as f:
            i = 1
            for item in self.res:
                f.write(
                    f"Товар №{i}\n\nНазвание: {item['title']}\n"
                    f"Ссылка: {item['href']}\n"
                    f"Цена: {item['price']}\n\n{'*' * 40}\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
