from bs4 import BeautifulSoup
import urllib.request
from time import sleep
from selenium import webdriver
from google import search

url = 'https://www.google.com/#q=ministry+of+lost+souls+lyrics'
url1 = 'https://www.google.com/search?q=crazy+train+lyrics'
source = urllib.request.urlopen (url).read ()
soup = BeautifulSoup(source, 'lxml')

# def test_code():
#     print(soup.prettify())
#     print(soup.text)
#
#     print(soup.title ,' ' ,  soup.title.name ,' ' , soup.title.string)
#
#     print(soup.find_all('div', class_='g'))
#
#     for div in soup.find_all('div',eid='MD1jWbzsIoi6jwT0j4nwBQ'):
#         print('lol')
#         print(div.text)
#
#     for div in soup.find_all('div',id='ires'):
#         print('lol1')
#         print(div.text)
#
#     for div in soup.find_all('div',eid='MD1jWbzsIoi6jwT0j4nwBQ'):
#         print('lol')
#         print(div.text)
#
#     for div in soup.find_all('div',attrs={'class':'g'}):
#         print('lol1')
#         print(div.text)
#
#     for links in soup.find_all('a'):
#         print(links.get('href'))
#
#     for tags in soup.find_all('div', class_='srg'):
#         print(tags)
#         for anc in tags.find_all('a'):
#             print(anc)

# def new():
#     d = webdriver.Chrome ('D:\Chrome Downloads\chromedriver_win32\chromedriver.exe')
#     d.get ('https://www.google.com/')
#     search = d.find_element_by_name ('q')
#     search.send_keys ('crazy train lyrics\n')
#     index = 0
#     links = []
#
#     elements = d.find_element_by_xpath("//h3//a")
#     print(elements)
#     for link in elements:
#         href = link.get_attribute("href")
#         links.append(href)
#     d.close()
#     print(links)
# # new()

def from_google():
    links = []
    count = 0
    for link in search(url1):
        print(link)
        count +=1
        links.append(link)
        if count == 20:
            break
    # print(links)
from_google()