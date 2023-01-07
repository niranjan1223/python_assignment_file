import Noidea.core.sample as Ni
import unittest
#create a class for testing

class test_disjoints(unittest.TestCase):
    def test_sample(self):
        result=Ni.disjoint([1,5,3],[3,1],[5,7])
        self.assertEqual(result,1)


if __name__ == '__main__':
    unittest.main()