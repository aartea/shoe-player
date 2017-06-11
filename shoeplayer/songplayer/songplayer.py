from user import User
import webbrowser

class SongPlayer(object):
    def __init__(self, username):
        self.user = User(username)
        self.playlist = []

    def add_to_playlist(self, song_name):
        self.playlist.append(song_name)

    def play_song(self):
        return webbrowser.open("smooth_criminal.mp3")
