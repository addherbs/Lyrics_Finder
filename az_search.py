from bs4 import BeautifulSoup
import urllib.request

# name = 'crazy train'
def generate_az_url(song_name):
    url = 'http://search.azlyrics.com/search.php?q='
    split = song_name.split(' ')
    lenght = len(split)
    count = 1
    generated_url = ''
    for word in split:
        if count==lenght:
            generated_url = generated_url + word
        else:
            generated_url = generated_url  + word + '+'
        count = count + 1
    generated_url = url + generated_url

    list_of_song_names, result_dictionary = changeInClass (generated_url)
    return list_of_song_names, result_dictionary

# final_url = generate_az_url()

def changeInClass(final_url):
    source = urllib.request.urlopen (final_url).read ()
    soup = BeautifulSoup (source, 'lxml')
    result_dictionary = {}
    count = 0
    for each_row in soup.find_all('td', class_='text-left visitedlyr'):
        count = count + 1
        if count ==6:
            break
        else:
            names = [names.text for names in each_row.find_all('b')]
            # print(names)
            link = each_row.find('a').get('href')
            artist_name = names[1]
            song_name = names[0]
            entire_song_name = str (song_name + ' By Artist ' + artist_name)
            # print(each_row.find('a').get('href'))
            # print('song ', names[0])
            # print ('artist ', names[1])
            # print(entire_song_name , ' ' , link)
            result_dictionary[entire_song_name] = link

    list_of_song_names = result_dictionary.keys()
    # print(list_of_song_names)
    return list_of_song_names, result_dictionary
    # for k,v in result_dictionary.items():
    #     print('key: ' , k ,' ==>' , 'value: ', v)

# changeInClass(final_url)


def scrape_az_for_links(final_url):
    source = urllib.request.urlopen (final_url).read ()
    soup = BeautifulSoup (source, 'lxml')
    list = []
    table = soup.table
    count = 0
    for anc in table.find_all ('a'):

        # print(anc)
        for b in anc.find_all('b'):
            print("b tags: ", b)
        title = anc.text.lower ()
        if (name.lower () == title):
            list.append (anc.get ('href'))
            print(anc.get('href'))
        print('------------------')
# print(table)
    return list

# az_search_result_links = scrape_az_for_links(final_url)

# print('------------------')
# print(az_search_result_links)