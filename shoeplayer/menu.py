#"Inspired from Cengage Fundamentals of Python"
from songplayer import SongPlayer
import pygame as pg


class Menu(object):

    QUIT = '7'
    COMMANDS = ('1','2','3','4','5','6')

    MENU = """
    1. search by title
    2. search by artist
    3. skip a song
    4. like or dislike a song
    5. save to playlist
    6. play a song
    7. quit program

    """

    def __init__(self, username):
        self.songplayer = SongPlayer(username)

        print"\n"
        print "Shoe Player: Music Simplified"
        while True:
            self.menu_display()
            if self.command == self.QUIT:
                print 'Exited shoe player.'
                break

    def menu_display(self):
        print self.MENU
        command = self.user_command()
        self.run_command(command)

    def user_command(self):
        while True:
            self.command = raw_input("Enter selection: ")
            if not self.command in self.COMMANDS and not self.command in self.QUIT:
                print "Error: Not a Valid Command."
            else:
                return self.command

    def run_command(self, command):


        if self.command == '1':
            #search song by Title
            print 'Option  1'
        elif self.command == '2':
            #search by artist
            print 'Option 2'
        elif self.command == '3':
            #skip song
            self.songplayer.skip_song()
        elif self.command == '4':
            #like or dislike song
            print 'Option  4'
        elif self.command == '5':
            #save to playlist
            print 'Option  5'
        elif self.command == '6':
            # play a song
            self.songplayer.play_song()
            while pg.mixer.music.get_busy():
                self.menu_display()
                if self.command == self.QUIT:
                    self.songplayer.stop_song
                    break
                pg.time.Clock().tick(0)
