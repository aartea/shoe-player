# -*- coding: utf-8 -*-
import sys
import pygame as pg
from user import User
from song import Song
#from progress.bar import Bar #Progress bar for UI

TRACKS = ["/home/aaron/Desktop/github/shoe-player/shoe-player/shoeplayer/resources/media/Hold_On_We_re_Going_Home_Ft_Majid_Jordan.ogg"\
            ,"/home/aaron/Desktop/github/shoe-player/shoe-player/shoeplayer/resources/media/Wu-Tang_Forever.ogg"]
track = 0

class SongPlayer(object):
#Load user definition, i.e. username with password
#to associate playlist (and hence, related songs) to specific user.
    def __init__(self, username):
        pg.init()
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

#Need a better way to play with effective path of song.
    def play_song(self):
        file_name = raw_input("Please input song name: ")
        try:
            pg.mixer.init()
            pg.mixer.music.load(file_name)
            pg.mixer.music.play()
            self.song.set_song_path(file_name)
        except IOError:
            print "Could not read file: ", file_name
            sys.exit


    def stop_song(self):
        pg.quit()

    def skip_song(self):
        self.stop_song()
        next_track = (track + 1)%len(TRACKS)
        pg.mixer.init()
        pg.mixer.music.load(TRACKS[next_track])
        pg.mixer.music.play()


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
