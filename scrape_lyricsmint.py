from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request

url = 'http://www.lyricsmint.com/2015/08/main-hoon-hero-tera-salman-khan.html'

req = Request (url, headers={'User-Agent': 'Mozilla/5.0'})
source = urlopen(req).read()
soup = BeautifulSoup (source, 'lxml')

def scrape_lm():
    list = []
    for lines in soup.find_all('div', id="lyric"):
        for p in lines.find_all('p'):
            string = str(p)
            # print(string)
            string = string.replace ('<p>', '')
            string = string.replace ('</p>', '')
            string = string.replace ('<br/>', '\n')
            list.append(string)
            list.append ('----------------------------')
            # print(string)
            # string = string.replace ('br/>', '\n')
            # print(string.replace('<br/>', '\n'))
            # print('-------------')

    # print(list)
    # for lines in list:
    #     print(lines)
    return list
