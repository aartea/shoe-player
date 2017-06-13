# -*- coding: utf-8 -*-
import webbrowser, shoeplayer, pygame, os
from user import User
from pygame import *


class SongPlayer(object):

#Load user definition, i.e. username with password
#to associate playlist (and hence, related songs) to specific user.

#Set of playlist operations
    def __init__(self, username):
        self.user = User(username)
        self.playlist = []

    def add_to_playlist(self, song_name):
        self.playlist.append(song_name)

#Set of song operations
#Other considerations for playing a song -- need to ensure input file follows PEP-263
#Or, input file string is viable to be used.
    def load_song(self, file_name):
        raw_input("Please input song name: ")
        try:
            mixer.init()
            mixer.music.load(file_name)
        except IOError:
            print "Could not read file: ", file_name
            sys.exit

    def play_song(self, song):
        mixer.music.play(song)

        while mixer.music.get_busy():
            time.Clock().tick(10)
    # def stop_song(self, file_name)

    # def skip_song(self, song)

#Search functionality
    # def find_title(self, song)

    #def find_artist(self, artist)

#User specific definitions
    #def like_song(self, song)

    #def create_playlist(self, playlist)


    #def destroy_playlist(self, playlist)

#file = "/home/aaron/Downloads/08_Hold_On_We_re_Going_Home_Ft_Majid_Jordan.ogg"

songplayer = SongPlayer("Aaron")
load_song = songplayer.load_song(file)
songplayer.play_song(load_song)
