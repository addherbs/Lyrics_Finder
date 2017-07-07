from flask import flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Enter the song name to find the lyrics associated with it'

if __name__ = '__main__'
    app.run()
