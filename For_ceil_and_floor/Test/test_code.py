import For_ceil_and_floor.core.sample as cf
import unittest
import numpy as np

class testsample(unittest.TestCase):
    def test_floor(self):
        array=np.array([1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9])
        result= cf.floor_arr(array)
        p=np.array([ 1.,2.,3.,4.,5.,6.,7.,8.,9.])
        self.assertIsNone(np.testing.assert_almost_equal(result,p,1))

    def test_ceil(self):
        array=np.array([1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9])
        result= cf.ceil_arr(array)
        q=np.array([2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])
        self.assertIsNone(np.testing.assert_almost_equal(result,q,1))

    def test_rint(self):
        array=np.array([1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9])
        result= cf.rint_arr(array)
        r=np.array([1.0,2.0,3.0,4.0,6.0,7.0,8.0,9.0,10.0])
        self.assertIsNone(np.testing.assert_almost_equal(result,r,1))
if __name__ == '__main__':
    unittest.main()