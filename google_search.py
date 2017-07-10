from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.google.com/#q='
name = 'ministry of lost souls'
suffix = 'lyrics'



def generate_google_url():
    split = name.split(' ')
    print(split)
    final_name = ''
    for word in split:
        final_name = final_name  + word + '+'
    final_name = final_name + suffix
    final_google_url = url + final_name
    print(final_google_url)

generate_google_url()
