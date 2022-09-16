import requests
from bs4 import BeautifulSoup


url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
all_articles = soup.find_all('article')

links = []
for article in all_articles:
    article_type = article.find('span', {'class': 'c-meta__type'}).text
    if article_type == 'News':
        links.append(article.find('a').get('href'))
full_link = ['https://www.nature.com' + link for link in links]
saved_articles = []
for link in full_link:
    r = requests.get(link)
    soup_l = BeautifulSoup(r.content, 'html.parser')
    l_content = soup_l.find('div', {'class': 'c-article-body'}).text.strip()
    file_name = soup_l.find('title').text.replace(' ', '_') + '.txt'
    saved_articles.append(file_name)
    with open(file_name, 'wb') as f:
        l_content_b = bytes(l_content, encoding='utf-8')
        f.write(l_content_b)

print(f'Saved articles: {saved_articles}')
