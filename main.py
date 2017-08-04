from flask import Flask, request, render_template
from az_scrape_lyrics import scrape_lyrics
from az_search import generate_az_url, changeInClass
from search_google_for_lm_songs import generate_lm_urls

app = Flask(__name__)
list_of_song_names = []
result_dictionary = {}


#Yo returned to file

@app.route('/', methods=['GET', 'POST'])
def index():
    global list_of_song_names,result_dictionary
    if request.method == 'GET':
        list_of_song_names = []
        return render_template('index.html' , name = '', list_of_song_names = list_of_song_names)
    elif request.method == 'POST':
        name = request.form.get('song')

        list_of_song_names, result_dictionary = generate_az_url(name)

        if bool(list_of_song_names) == False:
            hindi_song_result = generate_lm_urls(name)

            print(hindi_song_result)

        return render_template('index.html', name = name, list_of_song_names = list_of_song_names )

@app.route('/giveSongResult', methods=['GET', 'POST'])
def showLyrics():
    if request.method == 'GET':
        list_of_song_names = []
        return render_template('index.html' , name = '', list_of_song_names = list_of_song_names)
    elif request.method == 'POST':
        list_of_song_names = []
        key = request.form['songname']
        # print('key: ',key)
        link_value = result_dictionary[key]
        print(link_value)
        # print (link_value)

        lyrics = scrape_lyrics(link_value)
        lyrics_array = []

        for lines in lyrics:
            lyrics_array.append(lines)
        return render_template('song_lyrics.html' , song_lyrics = lyrics_array , song_name = key)

if __name__ == "__main__" :
    app.run()
