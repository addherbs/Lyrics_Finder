from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen


name = 'main tera hero'
def generate_az_url():
    url = 'http://www.lyricsmint.com/?s='
    final_name = ''
    split = name.split(' ')
    # print(split)
    final_name = ''
    lenght = len(split)
    # print(lenght)
    count = 1
    for word in split:
        # print (count)
        if count==lenght:
            final_name = final_name + word
        else:
            final_name = final_name  + word + '+'
        count = count + 1
    final_name = url + final_name
    return final_name

final_url = generate_az_url()
print(final_url)

def scrape_lyricsmint_for_links(final_url):
    # source = urllib.request.urlopen (final_url).read()
    req = Request (final_url, headers={'User-Agent': 'Mozilla/5.0'})
    source = urlopen(req).read()


    soup = BeautifulSoup (source, 'lxml')
    list = []
    # print(soup.prettify())
    # table = soup.table

    for anc in soup.find_all('a'):
        print('hello')
        print(anc)

        # print(anc.get('href'))
    # print(table)
    return list


az_search_result_links = scrape_lyricsmint_for_links(final_url)
print('------------------')
print(az_search_result_links)