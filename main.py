import os
import requests as rq
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
# please add your own keys, values in .env file and endpoints in the below URL
# TODO 〰〰〰〰〰〰〰〰〰〰 Extracting top 100 songs from billboard based on date 〰〰〰〰〰〰〰〰〰〰
date = input("For which date you want to search the list of songs YYYY-MM-DD\n")
response = rq.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
soup = BeautifulSoup(response.text, "html.parser")
all_songs = soup.select("li ul li h3")
songs_list = [song.getText(strip=True) for song in all_songs]

# TODO 〰〰〰〰〰〰〰〰〰〰 Spotify authentication 〰〰〰〰〰〰〰〰〰〰
sp_oauth = SpotifyOAuth(
    client_id=os.environ['SPOTIFY_CLIENT_ID'],
    client_secret=os.environ['SPOTIFY_CLIENT_SECRET'],
    redirect_uri=os.environ['SPOTIPY_REDIRECT_URI'],
    scope='playlist-modify-private',
    cache_path='.cache',
    show_dialog=True,
)
token_info = sp_oauth.get_cached_token()
access_token = token_info['access_token']
spotify = Spotify(access_token)
user_id = spotify.current_user()['id']
year = date.split("-")[0]
playlist = spotify.user_playlist_create(
    user=user_id,
    name=f"{date} LioTronic 100",
    public=False
)

# TODO 〰〰〰〰〰〰〰〰〰〰 Extracting links of each song by passing song name 〰〰〰〰〰〰〰〰〰〰
song_urls = []
for song in songs_list:
    song_result = spotify.search(q=f"track:{song} year:{year}", type="track")
    try:
        url = song_result["tracks"]["items"][0]["uri"]
    except IndexError:
        print(f'"{song}" does not exist in spotify so Skipped....')
    else:
        song_urls.append(url)

spotify.playlist_add_items(playlist_id=playlist["id"], items=song_urls)
print(f"Playlist created successfully with name {date} LioTronic 100")