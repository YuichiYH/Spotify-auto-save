import spotipy
import json
import sys
import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

def linkID(link: str) -> str:
    ID = link.split('/')[-1].split('?')[0]
    return ID


with open('token.json', 'r') as jsonFile:
    tokens = json.load(jsonFile)

username = sys.argv[1] 

scopes = ['playlist-read-private','playlist-read-collaborative','playlist-modify-private','playlist-modify-public']

try:
    token = util.prompt_for_user_token(username=username, client_id=tokens["client_id"], client_secret=tokens["client_secret"],redirect_uri="http://google.com/",scope=scopes)
except:
    os.remove(f".cache={username}")
    token = util.prompt_for_user_token(username=username, client_id=tokens["client_id"], client_secret=tokens["client_secret"],redirect_uri="http://google.com/",scope=scopes)

sp = spotipy.Spotify(auth=token)

targetPlaylist = sys.argv[2]
weeklyPlaylist = sys.argv[3]


# playlist = sp.user_playlist_tracks(username,"585bssFwz8FNsEaGFkKLrB",fields="tracks")
playlist = sp.user_playlist(username, "37i9dQZEVXcEOnezVigr6u",fields="tracks,next")
results = playlist['tracks']

track_ids = []

for i, item in enumerate(results['items']):
    track = item['track']
    track_ids.append(track['id'])

print(track_ids)

result = sp.playlist_add_items('4IUGAYFGwES21gNebDjClr',track_ids)