import webbrowser, shoeplayer
from user import User


class SongPlayer(object):

#Set of playlist operations
    def __init__(self, username):
        self.user = User(username)
        self.playlist = []

    def add_to_playlist(self, song_name):
        self.playlist.append(song_name)

#Set of song operations
    def play_song(self):
        return webbrowser.open("smooth_criminal.mp3")
