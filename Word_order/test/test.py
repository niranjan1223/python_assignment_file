import Word_order.core.sample as e
import unittest

class testcase(unittest.TestCase):
    def test_word(self):
        n=4
        w = 'bcdef',\
            'abcdefg',\
            'bcde',\
            'bcdef'
        o=3
        2,1,1
        result= e.word_order(n,w)
        self.assertEqual(result,o)

if __name__ == '__main__':
    unittest.main()