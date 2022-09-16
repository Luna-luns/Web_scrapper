import requests


if __name__ == '__main__':
    url = input('Input the URL:\n')
    r = requests.get(url)
    if not r:
        print(f'The URL returned {r.status_code}!')
        exit()
    with open('source.html', 'wb') as f:
        f.write(r.content)
    print('\nContent saved.')
