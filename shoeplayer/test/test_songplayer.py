import unittest, shoeplayer
from songplayer import SongPlayer


class TestSongPlayer(unittest.TestCase):
    def setUp(self):
        self.player = SongPlayer("Armen")

    def test_create_of_songplayer(self):
        self.assertEqual(self.player.user.username, "Armen")

    def test_adding_to_playlist(self):
        self.player.add_to_playlist("SmoothCriminal")
        self.assertEqual(len(self.player.playlist), 1)

    def test_play_song(self):
        self.assertEqual(self.player.play_song(),True)


if __name__ == '__main__':
    unittest.main()
