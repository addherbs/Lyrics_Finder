
from bs4 import BeautifulSoup
import urllib.request
from google import search
from urllib.request import Request, urlopen

url = 'http://www.lyricsted.com/search/?s=wajah+tum+ho'

req = Request (url, headers={'User-Agent': 'Mozilla/5.0'})
source = urlopen(req).read()
soup = BeautifulSoup (source, 'lxml')

for links in search('https://www.google.com/#q=lyricsmint.com+wajah+tum+ho+lyrics'):
    print(links)


# print(soup.prettify())
# print(soup.find_all('a'))
#
# for anc in soup.find_all('a'):
#     print(anc)