import unittest
import numpy as np
from gra import odczyt
import os

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'score.txt')


class Testy(unittest.TestCase):
    def setUp(self):
        self.testdata = open(TESTDATA_FILENAME).read()
        self.integer = int(self.testdata)
        self.base_integers = [0,1,2,3,4,5,6,7,8,9]

    def test_integers(self):
        self.assertIn(self.integer, self.base_integers)

    def test_speed(self):
        tmp=np.random.randint(5, 25)
        self.assertTrue(tmp >=5 and tmp <= 25)

    def test_szerokosc(self):
        SCREEN_WIDTH = 800
        width=np.random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100)
        self.assertTrue(width >= SCREEN_WIDTH + 20 and width <= SCREEN_WIDTH + 100)

    def test_wysokosc(self):
        SCREEN_HEIGHT = 600
        height=np.random.randint(0, SCREEN_HEIGHT)
        self.assertTrue(height >= 0 and height <= SCREEN_HEIGHT)

    def test_odczyt(self):
        self.assertTrue(odczyt(reading=True))
        self.assertFalse(odczyt(reading=True),"Plik zostal otworzony")



if __name__ == "__main__":
    unittest.main(verbosity=2)