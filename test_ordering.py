
# Writing a unit test (basic example)
# First - need to import unittest package
# Second - need to import class/functions from original code
# Second - set up a class that will define a bunch of functions to test original code
# Notice parameter for the class is unittest.TestCase
# See example below for what to put in each function
# To run the unit test, in the terminal type python3 -m unittest test_ordering

import unittest
from ordering import order

class testing_stuff(unittest.TestCase):

    def test_order(self):
        given = [5,3,2,1,8,14]
        expected = [1,2,3,5,8,14]
        actual = order(given)
        self.assertEqual(expected, actual)
    

if __name__ == '__main__':
    unittest.main()