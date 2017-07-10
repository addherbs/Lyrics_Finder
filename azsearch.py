from bs4 import BeautifulSoup
import urllib.request


name = 'crazy train'
def generate_az_url():
    url = 'http://search.azlyrics.com/search.php?q='
    final_name = ''
    split = name.split(' ')
    print(split)
    final_name = ''
    lenght = len(split)
    print(lenght)
    count = 1
    for word in split:
        print (count)
        if count==lenght:
            final_name = final_name + word
        else:
            final_name = final_name  + word + '+'
        count = count + 1
    final_name = url + final_name
    return final_name

final_url = generate_az_url()
print(final_url)


def scrape_az_for_links(final_url):
    source = urllib.request.urlopen (final_url).read ()
    soup = BeautifulSoup (source, 'lxml')
    list = []
    # print(soup.prettify())
    table = soup.table
    for anc in table.find_all('a'):
        # print(anc.text)
        title = anc.text.lower()
        if (name.lower() == title):
            list.append(anc.get('href'))

        # print(anc.get('href'))
    # print(table)
    return list


az_search_result_links = scrape_az_for_links(final_url)
print('------------------')
print(az_search_result_links)