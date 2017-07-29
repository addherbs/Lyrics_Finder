
from bs4 import BeautifulSoup
import urllib.request
# from google import search
from urllib.request import Request, urlopen

url = 'http://www.lyricsted.com/search/?s=wajah+tum+ho'

source = urllib.request.urlopen (url).read ()
soup = BeautifulSoup (source, 'lxml')

# print(soup.prettify())
count = 0
for out in soup.find_all ('div', class_='gsc-wrapper'):
    for a in out.find_all('a'):
        print(a)
