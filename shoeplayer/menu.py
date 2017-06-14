#"Inspired from Cengage Fundamentals of Python"
#Requirements
import os, os.path

QUIT = '9'
COMMANDS = ('1','2','3','4','5','6', '7','8')

MENU = """
1. search by title

2. search by artist

3. skip a song

4. like or dislike a song

7. save to playlist

8. play a song

9. quit program"""

def main():
    print "Shoe Player: Music Simplified"
    while True:
        print os.cwd()
        print MENU
        command = userCommand()
        runCommand(command)
        if command == QUIT:
            print 'Exited shoe player.'
            break

def userCommand()
    while True:
        command = raw_input("Enter selection: ")
        if not command in COMMANDS:
            print "Enter a valid number."
        else:
            return command

def runCommand(command):
    if command == '1':
        #search song by Title
    elif command == '2':
        #search by artist
    elif command == '3':
        #skip song
    elif command == '4':
        #like or dislike song
    elif command == '5':
