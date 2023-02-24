import spotipy
import json
import sys
import os
import datetime
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

if os.path.isfile('date.json'):

    with open('date.json', 'r') as dateFile:
        storageDate = json.load(dateFile)

        last_update = datetime.datetime.strptime(storageDate['date'], '%Y-%m-%d')
        today = datetime.datetime.today()
        if (last_update + datetime.timedelta(days = 7)) >= today:
            print('already added this playlist')
            sys.exit()

        else:
            x = {
                'year':today.strftime('%Y'),
                'month':today.strftime('%m'),
                'day':today.strftime('%d'),
                'date':str(datetime.date.today())
            }
    with open('date.json', 'w') as dateFile:
        json.dump(x, dateFile)
            


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

def linkID(link: str) -> str:
    ID = link.split('/')[-1].split('?')[0]
    return ID

def get_track_ids(playlist_ID: str) -> list:

    playlist = sp.user_playlist(username, playlist_ID, fields="tracks")
    tracks = playlist['tracks']

    track_ids = []

    for item in tracks['items']:
        track = item['track']
        track_ids.append(track['id'])

    return track_ids


targetPlaylist_ID = linkID(sys.argv[2])
weeklyPlaylist_ID = linkID(sys.argv[3])
