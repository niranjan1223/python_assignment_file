import Linearalgebra.core.sample as la
import unittest


class MyTestCase(unittest.TestCase):
    def test_array(self):
        arr=[[1.1,1.1],[1.1,1.1]]
        result=la.linear_algebra(arr)
        self.assertEqual(result,0.0)

if __name__ == '__main__':
    unittest.main()