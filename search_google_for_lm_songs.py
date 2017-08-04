from google import search

url = 'https://www.google.com/#q='
prefix = 'www.lyricsmint.com'
name = 'wajah tum ho'
suffix = 'lyrics'

def generate_lm_urls(SongNameInput):
    split = SongNameInput.split(' ')

    final_name = prefix + '+'
    for word in split:
        final_name = final_name  + word + '+'

    final_name = final_name + suffix
    final_google_url = url + final_name

    # Calling to generate google search links
    dictionary = from_google(final_google_url)
    return dictionary



def from_google(final_google_url):
    links = []
    count = 0
    print(final_google_url)
    for link in search(final_google_url):
        # print(link)
        count +=1
        links.append(link)
        if count == 5:
            break

    print(links)

    # Calling to generate dictionary
    dictionary = generate_song_names_from_url (links)


    return dictionary


# links = from_google(final_url)

def generate_song_names_from_url(links):
    dict = {}
    for link in links:
        split = link.split('/')
        if str(split[2]) == prefix:
            if len(split) == 6:
                name = str(split[5].split('.html')[0])

                name_split = name.split('-')
                final_name=''
                for word in name_split:
                    final_name = final_name + word + ' '
                final_name = final_name.strip().title()
                print(final_name)
                print(link)
                dict[final_name] = link

    for key,value in dict.items():
        print('key: ' , key , 'value: ',value)
        print('-----------')

    return dict

# generate_song_names_from_url(links)
# dic = generate_lm_urls('wajah tum ho')