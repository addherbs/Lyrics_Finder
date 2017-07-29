from google import search

url = 'https://www.google.com/#q='
prefix = 'www.lyricsmint.com'
name = 'wajah tum ho'
suffix = 'lyrics'

def generate_lm_urls():
    split = name.split(' ')
    # print(split)
    final_name = prefix + '+'
    for word in split:
        final_name = final_name  + word + '+'
    # final_name = final_name
    final_name = final_name + suffix
    final_google_url = url + final_name
    # print(final_google_url)
    return final_google_url
final_url = generate_lm_urls()

def from_google(final_url):
    links = []
    count = 0
    print(final_url)
    for link in search(final_url):
        # print(link)
        count +=1
        links.append(link)
        if count == 5:
            break
    # print(links)
    return links
links = from_google(final_url)

print(links)


def generate_song_names_from_url(links):
    dict = {}
    for link in links:
        split = link.split('/')
        if str(split[2]) == prefix:
            if len(split) == 6:
                name = str(split[5].split('.html')[0])
                # print(name)
                name_split = name.split('-')
                final_name=''
                for word in name_split:
                    final_name = final_name + word + ' '
                final_name = final_name.strip().title()
                print(final_name)
                print(link)
                dict[final_name] = link

            # print(split[2])
            # print(split[2])
                # print (split[5])
    # print(dict)
    for key,value in dict.items():
        print('key: ' , key , 'value: ',value)
        # print(value)
        print('-----------')


generate_song_names_from_url(links)
