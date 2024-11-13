import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World from Aya Al Baba"), "Hello, World from Aya Al Baba!")
if __name__ == "__main__":
    unittest.main()