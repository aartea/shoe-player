#Main driver class: app.py
#Description: Entry point into the program.
from songplayer import SongPlayer
import webbrowser, shoeplayer, pygame, os

#file = "/home/aaron/Downloads/08_Hold_On_We_re_Going_Home_Ft_Majid_Jordan.ogg"


#Implement CLI menu options

songplayer = SongPlayer("Aaron")
songplayer.play_song()
# songplayer.play_song()
