# -*- coding: utf-8 -*-
import webbrowser, shoeplayer, pygame
from user import User
from pygame import *


class SongPlayer(object):

#Set of playlist operations
    def __init__(self, username):
        self.user = User(username)
        self.playlist = []

    def add_to_playlist(self, song_name):
        self.playlist.append(song_name)

#Set of song operations
#Other considerations for playing a song -- need to ensure input file follows PEP-263
#Or, input file string is viable to be used.
    def play_song(self, file_name):
        raw_input("Please input song name: ")
        mixer.init()
        mixer.music.load(file_name)
        mixer.music.play()

        while mixer.music.get_busy():
            time.Clock().tick(10)
    def stop_song(self, file_name)

file = "/home/aaron/Downloads/08_Hold_On_We_re_Going_Home_Ft_Majid_Jordan.ogg"

songplayer = SongPlayer("Aaron")
songplayer.play_song(file)
