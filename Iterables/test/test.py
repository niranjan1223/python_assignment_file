import Iterables.core.sample as i
import unittest

class testcase(unittest.TestCase):
    def test_Iterate(self):
        size=4
        input=['a','a','c','d']
        k=2
        result= i.iterate_module(size,input,k)
        self.assertEqual(result,'0.833')

if __name__ == '__main__':
    unittest.main()





