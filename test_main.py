# test_main.py
import unittest
from main import greet_person

class TestMain(unittest.TestCase):
    def test_greet_person(self):
        self.assertEqual(greet_person("Kyle"), "Hello, Kyle!")
        self.assertEqual(greet_person("Morgan"), "Hello, Morgan!")

if __name__ == "__main__":
    unittest.main()