from Handling_Data import *
import unittest


class Test_Functions(unittest.TestCase):
    """
    Class object to test the handling data functions
    """

    def test_get_information(self):
        """
        Checks the id aquired for bulbasaur is correct from the get_information function
        """
        self.assertEqual(get_information("Bulbasaur")["id"], 1)

    def test_key_information_parsing(self):
        """
        Checks the information aquired in the key_information_parsing function is correct
        """
        self.assertEqual(key_information_parsing("Bulbasaur")[1], "Bulbasaur")
        self.assertEqual(key_information_parsing("Bulbasaur")[5], 1)
        self.assertEqual(len(key_information_parsing("Bulbasaur")), 8)



