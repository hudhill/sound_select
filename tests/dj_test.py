import unittest
from models.dj import Dj

class TestDj(unittest.TestCase):
    
    def setUp(self):
        self.dj = Dj("Sam Hill", "sam.jpeg")
    
    def test_dj_has_name(self):
        self.assertEqual("Sam Hill", self.dj.name)
               
    def test_dj_has_image(self):
        self.assertEqual("sam.jpeg", self.dj.img)    
    