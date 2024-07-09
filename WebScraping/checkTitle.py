from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as httpError:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        # вызываем имя html тега
        title = bs.body.h1
    except AttributeError as atrError:
        return None
    return title

if __name__ == '__main__':
    title = getTitle('http://pythonscraping.com/pages/page1.html')
    if title == None:
        print('Title could not be found')
    else:
        print(title)
