import unittest
import Mutations.core.sample as m

class Testsample_mutations(unittest.TestCase):
    def test_mutations(self):
        result = m.mutate_string('abracadabra',5,'k')
        self.assertEqual(result,'abrackdabra')


if __name__=='__main__':
    unittest.main()