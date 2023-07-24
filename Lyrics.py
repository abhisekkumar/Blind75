import requests


def fetch_lyrics(artist, song):
    artist = artist.replace(' ', '%20')
    song = song.replace(' ', '%20')
    url = f'https://api.lyrics.ovh/v1/{artist}/{song}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['lyrics']
    elif response.status_code == 404:
        return f"Lyrics for {artist.replace('%20', ' ')} - {song.replace('%20', ' ')} not found."
    else:
        return f"Error: received status code {response.status_code}"


print("Welcome to the Lyrics Finder!")

artist = input("Enter the artist's name: ")
song = input("Enter the song's name: ")

lyrics = fetch_lyrics(artist, song)
print(lyrics)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
