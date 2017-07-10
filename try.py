from bs4 import BeautifulSoup
import urllib.request

google_url = 'https://www.google.com/#q=craazy+train+lyrics'
url = 'http://www.azlyrics.com/lyrics/ozzyosbourne/crazytrain.html'
song_name = input('Enter the Song Name:')



source = urllib.request.urlopen(url).read()
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())
count =0
for out in soup.find_all('div' , class_="container main-page"):
    for inn in out.find_all ('div'):
        count = count +1
        if count == 11:
            song_lyrics = inn.text

print(song_lyrics)