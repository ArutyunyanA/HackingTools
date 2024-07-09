from urllib.request import urlopen
from bs4 import BeautifulSoup

def cssScrape(url):
    html = urlopen(url).read()
    bs = BeautifulSoup(html, 'html.parser')
    # вызываем искать всё имея тега с атрибутами тега
    name_list = bs.find_all('span', {'class':'green'})
    for char in name_list:
        print(char.get_text())
if __name__ == '__main__':
    cssScrape('http://pythonscraping.com/pages/warandpeace.html')

   