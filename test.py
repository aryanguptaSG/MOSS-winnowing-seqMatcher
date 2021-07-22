from posixpath import abspath
import unittest
import winnowing
from os import path


# getting the path of file 
def setUp(file):
    return path.abspath(f'tests/{file}')


class TestWinnowing(unittest.TestCase):
    # testing for R language
    def test1(self):
        check = winnowing.Winnowing(file1=setUp("test6.r"),file2=setUp("test7.r"),lang="r")
        self.assertEqual(round(check.jaccardCheck(),2),0.91)
        self.assertEqual(round(check.plagiarismRate(),2),0.91)

    # testing for Python language
    def test2(self):
        check = winnowing.Winnowing(file1= setUp("test2.py"),file2=setUp("test3.py"),lang="py")
        self.assertEqual(round(check.jaccardCheck(),2),0.57)
        self.assertEqual(round(check.plagiarismRate(),2),0.57)
    
    # testing for C++ language
    def test3(self):
        check = winnowing.Winnowing(file1=setUp("test4.cpp"),file2=setUp("test5.cpp"),lang="cpp")
        self.assertEqual(round(check.jaccardCheck(),2),0.57)
        self.assertEqual(round(check.plagiarismRate(),2),0.57)

    # testing for Java language
    def test4(self):
        check = winnowing.Winnowing(file1= setUp("test8.java"),file2=setUp("test9.java"),lang="java")
        self.assertEqual(round(check.jaccardCheck(),2),1.00)
        self.assertEqual(round(check.plagiarismRate(),2),1.00)

    # testing with different type of files
    def test5(self):
        self.assertRaises(Exception,winnowing.Winnowing,file1=setUp("test2.py"),file2=setUp("test8.java"),lang="py")

    # testing with empty files
    def test6(self):
        self.assertRaises(Exception,winnowing.Winnowing,file1=setUp("test1.txt"),file2=setUp("test1.txt"),lang="r")
        
    # testing without passing language 
    def test6(self):
        self.assertRaises(Exception,winnowing.Winnowing,file1=setUp("test2.py"),file2=setUp("test3.py"))

    # testing with invalid arguments
    def test7(self):
        self.assertRaises(Exception,winnowing.Winnowing,rendom=setUp("test2.py"),file2=setUp("test3.py"),language="py")



if __name__ == '__main__':
    unittest.main()