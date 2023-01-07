# unittest for arthimatic mean , variance, median
import mean_var_std.core.sample as s
import unittest
import numpy as np


class test_sample(unittest.TestCase):
    # unit test for arthimatic mean
    def test_mean(self):
        array=np.array([[1,2],[3,4]])
        result=s.arr_mean(array)
        p = np.array([1.5,3.5])
        self.assertIsNone(np.testing.assert_almost_equal(result,p,1))

    # unittest for variance
    def test_var(self):
        array=np.array([[1,2],[3,4]])
        q=np.array([1.,1.])
        result=s.arr_var(array)
        self.assertIsNone(np.testing.assert_almost_equal(result,q,1))

    # unittest for standard deviation
    def test_std(self):
        arr=np.array([[1,2],[3,4]])
        result=s.arr_std(arr)
        self.assertEqual(result,1.11803398875)

if __name__ == '__main__':
    unittest.main()