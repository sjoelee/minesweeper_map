from __future__ import print_function
from Minefield import Minefield
import unittest

class MainClassTestCase(unittest.TestCase):

    def testSimpleMinefield(self):
        field = Minefield.process('5x5\n'
                                  '0,0\n'
                                  '1,0\n'
                                  '2,2\n'
                                  '4,4\n')
        expected = ("X X 1 0 0\n"
                    "2 3 2 1 0\n"
                    "0 1 X 1 0\n"
                    "0 1 1 2 1\n"
                    "0 0 0 1 X")
        
        assert field == expected

    def testAllMines(self):
        field = Minefield.process('2x3\n'
                                  '0,0\n'
                                  '1,0\n'
                                  '0,1\n'
                                  '1,1\n'
                                  '1,2\n'
                                  '0,2\n')
        expected = ("X X\n"
                    "X X\n"
                    "X X")
        assert field == expected

    def testSmallMineField(self):
        field = Minefield.process('1x1\n'
                                  '0,0\n')
        expected = "X"
        assert field == expected

    def testNoMinesSmall(self):
        field = Minefield.process('1x1\n')
        expected = "0"
        assert field == expected

    def testNoMines(self):
        field = Minefield.process('3x2\n')
        expected = ("0 0 0\n"
                    "0 0 0")
        assert field == expected

    def testInvalidSize(self):
        with self.assertRaises(ValueError):
            Minefield.process('0x5\n'
                              '0,0\n')

    def testInvalidMine(self):
        with self.assertRaises(ValueError):
            Minefield.process('5x5\n'
                              '0,0\n'
                              '1,5\n'
                              '2,2\n'
                              '4,4\n')
    
    def testEmptyInput(self):
        assert Minefield.process('') == ''
                     
if __name__== '__main__':
    unittest.main()
#     minefield = Minefield()
# #    minefield.process('')
#     minefield.process('5x5\n'
#                       '0,0\n'
#                       '1,5\n'
#                       '2,2\n'
#                       '4,4\n')
