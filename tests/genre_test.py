import unittest
from models.genre import Genre

class TestGenre(unittest.TestCase):
    
    def setUp(self):
        self.genre = Genre("No Wave", "#000000")
    
    def test_genre_has_name(self):
        self.assertEqual("No Wave", self.genre.name)
               
    def test_genre_has_color(self):
        self.assertEqual("#000000", self.genre.color) 