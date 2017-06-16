#Main driver class: app.py
#Description: Entry point into the program.
import menu
from songplayer import SongPlayer

#file = "/home/aaron/Desktop/github/shoe-player/shoe-player/shoeplayer/resources/media/Hold_On_We_re_Going_Home_Ft_Majid_Jordan.ogg"


#Implement CLI menu options

#Validate username here and then continue with app.
username = raw_input("Log-in: ")
user = SongPlayer(username)
#Using log-in helper
menu = menu.Menu(user)
