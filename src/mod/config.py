import json
from os import path

class Config:
    def __init__(self, username=None, targetPlaylist=None, storagePlaylist=None):
      self.username = username
      self.targetPlaylist = targetPlaylist
      self.storagePlaylist = storagePlaylist
      self.file = {
          'username': self.username,
          'targetPlaylist': self.targetPlaylist,
          'storagePlaylist': self.storagePlaylist
       }
    
    def setUserneame(self, username):
       self.username = username
       self.file['username'] = username

    def getUsername(self):
       return self.username

    def setTargetPlaylist(self, playlist):
       self.targetPlaylist = playlist
       self.file['targetPlaylist'] = playlist

    def getTargetPlaylist(self):
       return self.targetPlaylist

    def setStoragePlaylist(self, playlist):
       self.storagePlaylist = playlist
       self.file['storagePlaylist'] = playlist

    def getStoragePlaylist(self):
       return self.storagePlaylist

    def save(self):
        if not path.isfile('json/config.json'):
            print('No config file found, creating a new one...')

    def load(self):
        if not path.isfile('json/config.json'):
            print('No config file found, creating a new one...')

        else:
            with open('json/config.json') as configFile:
                try:
                    configData = json.load(configFile)

                    self.username = configData['username']
                    self.targetPlaylist = configData['targetPlaylist']
                    self.storagePlaylist = configData['storagePlaylist']
                except:
                    print("Error on loading file, it appears to be corrupted")