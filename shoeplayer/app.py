#Main driver class: app.py
#Description: Entry point into the program.

import webbrowser, shoeplayer, pygame, os

#file = "/home/aaron/Downloads/08_Hold_On_We_re_Going_Home_Ft_Majid_Jordan.ogg"

songplayer = SongPlayer("Aaron")
load_song = songplayer.load_song(file)
songplayer.play_song(load_song)
