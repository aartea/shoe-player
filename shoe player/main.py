from user import User
from songplayer import SongPlayer

def start_app():
    player = SongPlayer("Armen")
    player.add_to_playlist("SmoothCriminal")

if __name__ == '__main__':
    start_app()
