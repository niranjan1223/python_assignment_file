import Runner_up_score.core.sample as r
import unittest
class testcase(unittest.TestCase):
    def test_sec_max(self):
        k=[2,3,6,6,5]
        result= r.runner_score(k)
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()