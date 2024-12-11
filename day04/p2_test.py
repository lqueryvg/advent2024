import unittest
import p2 as p
#from .p2 import checkCross, grid

class TestCheckCross(unittest.TestCase):
    def setUp(self):
        #global grid
        p.grid = [
            ['M', 'S', 'S', 'S'],
            ['S', 'A', 'M', 'S'],
            ['M', 'S', 'S', 'S'],
            ['S', 'M', 'S', 'M']
        ]

    # def test_checkCross_center(self):
    #     self.assertTrue(checkCross(1, 1, 'MSMS'))

    def test_checkCross_top_left(self):
        self.assertFalse(p.checkCross(0, 0, 'MSMS'))

    def test_checkCross_top_right(self):
        self.assertFalse(p.checkCross(0, 3, 'MSMS'))

    def test_checkCross_bottom_left(self):
        self.assertFalse(p.checkCross(3, 0, 'MSMS'))

    def test_checkCross_bottom_right(self):
        self.assertFalse(p.checkCross(3, 3, 'MSMS'))

    def test_checkCross_invalid_chars(self):
        self.assertFalse(p.checkCross(1, 1, 'XXXX'))

    def test_checkCross_out_of_bounds(self):
        self.assertFalse(p.checkCross(5, 5, 'MSMS'))

if __name__ == '__main__':
    unittest.main()
