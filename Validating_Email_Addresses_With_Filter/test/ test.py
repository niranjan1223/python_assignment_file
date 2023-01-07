import unittest
import  Validating_Email_Addresses_With_Filter.core.sample as e

class testsample_fun(unittest.TestCase):
    def test_email(self):
        s=('brian-23@hackerrank.com')
        result = e.filter_email(s)
        self.assertEqual(result,True)


if __name__=='__main__':
    unittest.main()
