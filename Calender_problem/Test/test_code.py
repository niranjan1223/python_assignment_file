import unittest
import Calender_problem.core.sample as c

#create a class for test the code

class Testsample_calender(unittest.TestCase):
    def calender(self):
        result = c.calen(month=8, day=5, year=2015)
        self.assertEqual(result, 'WEDNESDAY')


if __name__ == '__main__':
    unittest.main()