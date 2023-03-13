import spotipy
import sys
import os
import spotipy.util as util

import mod.checks as checks
import mod.config as config

# check if there is a json dir
checks.checkJson()

# Check if there is a date file and update it
checks.checkDate()

# Check if the client tokens exists and store's it
tokens = checks.getToken()

username = sys.argv[1] 

scopes = ['playlist-read-private','playlist-read-collaborative','playlist-modify-private','playlist-modify-public']

# Get the spotify auth
try:
    token = util.prompt_for_user_token(username=username, client_id=tokens["client_id"], client_secret=tokens["client_secret"],redirect_uri="https://github.com/YuichiYH/Spotify-auto-save/blob/main/redirect/README.md",scope=scopes)
except:
    os.remove(f".cache={username}")
    token = util.prompt_for_user_token(username=username, client_id=tokens["client_id"], client_secret=tokens["client_secret"],redirect_uri="https://github.com/YuichiYH/Spotify-auto-save/blob/main/redirect/README.md",scope=scopes)

sp = spotipy.Spotify(auth=token)

# Get the ID of a link, it can be from both music and playlist ids
def linkID(link: str) -> str:
    ID = link.split('/')[-1].split('?')[0]
    return ID

# get all the tracks (limit 100 tracks) from the playlist and return a list with their ids
def get_track_ids(playlist_ID: str) -> list:

    # Gets all the playlist tracks
    # Note: Mind that Spotipy has a limit of 100 tracks selected
    # Must find a way to get over that limit
    playlist = sp.user_playlist(username, playlist_ID, fields="tracks")
    tracks = playlist['tracks']

    track_ids = []

    for item in tracks['items']:
        track = item['track']
        track_ids.append(track['id'])

    return track_ids

# get the playlist IDs by their links
targetPlaylist_ID = linkID(sys.argv[2])
weeklyPlaylist_ID = linkID(sys.argv[3])

# get the tracks id into a list
track_ids = get_track_ids(targetPlaylist_ID)


# Add the list of tracks to the target playlist

result = sp.playlist_add_items(weeklyPlaylist_ID, track_ids)