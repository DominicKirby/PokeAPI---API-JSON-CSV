from Handling_Data import *
import unittest


class Test_Functions(unittest.TestCase):
    def test_get_information(self):
        self.assertEqual(get_information("Bulbasaur")["id"], 1)

    def test_key_information_parsing(self):
        self.assertEqual(key_information_parsing("Bulbasaur")[1], "Bulbasaur")
        self.assertEqual(key_information_parsing("Bulbasaur")[5], 1)
        self.assertEqual(len(key_information_parsing("Bulbasaur")), 8)



