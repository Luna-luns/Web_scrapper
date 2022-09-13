import requests
from link_error import LinkError
from bs4 import BeautifulSoup


try:
    url = input('Input the URL:\n')
    if 'title' not in url or 'imdb' not in url:
        raise LinkError
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    title = soup.find('h1').text
    des = soup.find('span', {'data-testid': 'plot-l'}).text
    if not des:
        raise LinkError
    movie = {'title': title, 'description': des}
    print(movie)
except LinkError as error:
    print(error)
