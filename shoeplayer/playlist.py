class Playlist(object):
    def __init__(self, playlist):
        self.playlist = playlist

#Record playlist name to csv
#Need to associate with user name...
#Considerations: User will have to define a playlist first, and
#then add a song, so the scheme is: user > begets playlist >
#begets song.
    #def save_playlist(self, playlist):
