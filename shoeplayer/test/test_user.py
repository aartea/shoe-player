import unittest, user
from user import User

class UserTest(unittest.TestCase):

    def test_adding_to_playist(self):
        user = User("Armen")
        self.assertEqual(user.username, "Armen")

if __name__ == '__main__':
    unittest.main()
