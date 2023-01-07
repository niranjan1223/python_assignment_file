import Minandmax.core.sample as mm
import unittest

class testsample(unittest.TestCase):
    def test_mutations(self):
        Ans=[[4,2],[2,5],[3,7],[1,3],[4,0]]
        result= mm.min_max(Ans)
        self.assertEqual(result,3)

if __name__ == '__main__':
    unittest.main()