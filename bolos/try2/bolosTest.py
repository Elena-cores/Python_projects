import unittest
from bolosLib import *

class BolosTest(unittest.TestCase):
    def test_gutter(self):
        self.assertEqual(evaluation("- - - - - - - - - -"), 0)
    
    def test_all_ones(self):
        self.assertEqual(evaluation("1-1 1-1 1-1 1-1 1-1 1-1 1-1 1-1 1-1 1-1"), 20)

    def test_spare(self):
        self.assertEqual(evaluation("5-5 1-1 - 0-10 2-4 - - - - -"), 31)
    
    def test_strike(self):
        self.assertEqual(evaluation("10- 2-3 1-1 1-1 - - - - - -"), 24)
    
    def test_two_consec_strikes(self):
        self.assertEqual(evaluation("10- 10- 4-2 - - - - - - -"), 46)

    def test_three_consec_strikes(self):
        self.assertEqual(evaluation("10- 10- 10- 1-1 - - - - - -"), 65)
    
    def test_strike_and_spare(self):
        self.assertEqual(evaluation("10- 5-5 - - - - - - - -"), 30)

    def test_complete_game(self):
        self.assertEqual(evaluation("4-2 9- 3-3 5-4 4-4 1-1 -6 10- 2-3 2-4"), 72)
    
    def test_bonus_strike(self):
        self.assertEqual(evaluation("- - - - - - - - - 10-10-10"), 30)

    def test_bonus_spare(self):
        self.assertEqual(evaluation("- - - - - - - - - 5-5-3"), 13)
    
    #def test_invalid_letters_rounds(self):
     #    with self.assertRaises(ValueError):
      #      evaluation('- - y- x-x - - - - w- w-')
    
    def test_excess_number_rounds(self):
         with self.assertRaises(NumberOfRounds):
            evaluation('- - - - - - - - - - - 2-2')

# run file as script 
if __name__ == '__main__': 
    unittest.main()
