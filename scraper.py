import requests
import os
from bs4 import BeautifulSoup


page_number = int(input())
art_type = input()
url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020'

for i in range(1, page_number + 1):
    os.mkdir(f'Page_{i}')
    os.chdir(f'./Page_{i}')
    r = requests.get(url, params={'page': f'{i}'})

    soup = BeautifulSoup(r.content, 'html.parser')
    all_articles = soup.find_all('article')
    links = []
    for article in all_articles:
        article_type = article.find('span', {'class': 'c-meta__type'}).text
        if article_type == art_type:
            links.append(article.find('a').get('href'))
    full_link = ['https://www.nature.com' + link for link in links]

    for link in full_link:
        r = requests.get(link)
        soup_l = BeautifulSoup(r.content, 'html.parser')
        l_content = soup_l.find('div', {'class': 'c-article-body'}).text.strip()
        file_name = soup_l.find('title').text.replace(' ', '_') + '.txt'
        with open(file_name, 'wb') as f:
            l_content_b = bytes(l_content, encoding='utf-8')
            f.write(l_content_b)
    os.chdir('..')

print('Saved all articles.')
