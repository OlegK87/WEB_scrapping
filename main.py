import bs4
import requests
from fake_useragent import UserAgent
ua = UserAgent()

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Jenkins', 'Guido']

base_url = 'https://habr.com'
url = base_url + '/ru/all/'

header = {'User-Agent':str(ua.chrome)}

response = requests.get(url, headers=header)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all("article")


for article in articles:
    words = article.find_all(class_='tm-article-body tm-article-snippet__lead')
    words = [word.text.strip() for word in words]
    for word in words:
        if any(element in word for element in KEYWORDS):
            title = (f"Название статьи - '{article.find('h2').find('span').text}'")
            data = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['datetime']
            data1 = f"Дата статьи - {data[0:10]} {data[12:19]}"
            link = (f"Ссылка на статью -{base_url + article.find(class_='tm-article-snippet__readmore').attrs['href']}")
            print(f"{data1}, {title}, {link}")



