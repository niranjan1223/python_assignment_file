import finding_percentage.core.sample as fp
import unittest

#create a class for unittest test begin
class testsample(unittest.TestCase):
    def test_percentage_1(self):
        student_marks = {'harsh': [25, 26.5, 28], 'Anurag': [26, 28, 30]}
        query_name = 'harsh'
        result= fp.percentage(student_marks,query_name)
        self.assertEqual(result,26.50)
    def test_percentage_2(self):
        student_marks = {'Krishna': [67,68,69], 'Arjun': [70,98,63],'Malika':[52,56,60]}
        query_name = 'Malika'
        result= fp.percentage(student_marks,query_name)
        self.assertEqual(result,56.0)

if __name__ == '__main__':
    unittest.main()
