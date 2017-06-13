# -*- coding: utf-8 -*-
from user import User
from pygame import *


class SongPlayer(object):

#Load user definition, i.e. username with password
#to associate playlist (and hence, related songs) to specific user.
    def __init__(self, username):
        self.user = User(username)
        self.playlist = []

#Read all song files from a source directory and store information
#to csv file? Or, have user load song and store it to csv..



#Set of song operations
#Other considerations for playing a song -- need to ensure input file follows PEP-263
#Or, input file string is viable to be used.

#load_song will load a song as well as store song name (path to song)
#to csv file, as well as associate it with the user name. So when
#a song is added to a playlist, the playlist will also have a
#relationship with the user.

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
    # def find_title(self, song)    #regex capabilities here.

    #def find_artist(self, artist)  #regex capabilities here.

##User specific definitions

##Set of playlist operations

    def add_to_playlist(self, song_name):
        self.playlist.append(song_name)


    #def create_playlist(self, playlist)


    #def destroy_playlist(self, playlist)

#User can like a song and it will be stored as their preference
#Reminder: under favorite song (ie 'like') of type boole, either true, false, or empty
#if empty, no preference and song will be played; else, if true, song will be played,
#else, if false, song will be skipped!

    #def like_song(self, song)
