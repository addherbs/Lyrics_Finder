from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.google.com/#q='
name = 'ministry of lost souls'
suffix = 'lyrics'




split = name.split(' ')
print(split)

final_name = ''
for word in split:
    final_name = final_name  + word + '+'

print(final_name + suffix)

final_name = final_name + suffix