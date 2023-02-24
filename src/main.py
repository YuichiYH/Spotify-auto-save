import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

with open('token.json', 'r') as jsonFile:
    tokens = json.load(jsonFile)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=tokens['client_id'],
                                                           client_secret=tokens['client_secret']))



