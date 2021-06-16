import unittest
from models.mix import Mix
from models.genre import Genre
from models.dj import Dj

class TestMix(unittest.TestCase):
    
    def setUp(self):
        self.mix = Mix("New Mix", "grating", "mix.jpeg", "tracklist.jpeg", "angular,jarring", "soundcloud.com", Genre("No Wave", "#000000"), Dj("Sam Hill", "image.jpeg"), False)
    
    def test_mix_has_title(self):
        self.assertEqual("New Mix", self.mix.title)
               
    def test_mix_has_description(self):
        self.assertEqual("grating", self.mix.description) 

    def test_mix_has_mix_img(self):
        self.assertEqual("mix.jpeg", self.mix.mix_img)

    def test_mix_has_tracklist_img(self):
        self.assertEqual("tracklist.jpeg", self.mix.tracklist_img)

    def test_mix_has_genre_tags(self):
        self.assertEqual("angular,jarring", self.mix.genre_tags)

    def test_has_audio_link(self):
        self.assertEqual("soundcloud.com", self.mix.audio_link)

    def test_mix_has_genre(self):
        self.assertEqual("No Wave", self.mix.genre.name)

    def test_mix_has_dj(self):
        self.assertEqual("Sam Hill", self.mix.dj.name)

    def test_mix_has_mysource(self):
        self.assertEqual(False, self.mix.mysource)