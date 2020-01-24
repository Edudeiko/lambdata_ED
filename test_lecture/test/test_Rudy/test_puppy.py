import unittest
from puppy import Puppy, PUPPIES  # Import almost anything created in your .py scriptimport unittest
import random


class TestPuppies(unittest.TestCase):

    def test_MakeUpper(self):
        # set-up
        pup = random.choice(PUPPIES)  # This is just here to be fancy
        pedro = Puppy("James", 3)  # What ever class you bring in...
        self.assertEqual(pedro.make_upper(), "JAMES")

if __name__ == "__main__":
    unittest.main()
