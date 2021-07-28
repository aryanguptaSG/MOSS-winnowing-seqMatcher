import unittest
import winnowing
from os import path


class TestWinnowing(unittest.TestCase):
    # setting the path of file 
    def setUp(self):
        self.r1 = path.abspath(f'tests/test6.r')
        self.r2 = path.abspath(f'tests/test7.r')
        self.python1 = path.abspath(f'tests/test2.py')
        self.python2 = path.abspath(f'tests/test3.py')
        self.cpp1 = path.abspath(f'tests/test4.cpp')
        self.cpp2 = path.abspath(f'tests/test5.cpp')
        self.java1 = path.abspath(f'tests/test8.java')
        self.java2 = path.abspath(f'tests/test9.java')
        self.emptyfile = path.abspath(f'tests/test1.txt')


    ''' Tesing With Path of Files .'''

    # testing for R language
    def testForR_Path(self):
        check = winnowing.Winnowing(file1=self.r1,file2=self.r2,lang="r")
        self.assertEqual(round(check.jaccardCheck(),2),0.91)
        self.assertEqual(round(check.plagiarismRate(),2),0.91)

    # testing for Python language
    def testForPython_Path(self):
        check = winnowing.Winnowing(file1= self.python1,file2=self.python2,lang="py")
        self.assertEqual(round(check.jaccardCheck(),2),0.57)
        self.assertEqual(round(check.plagiarismRate(),2),0.57)
    
    # testing for C++ language
    def testForCpp_Path(self):
        check = winnowing.Winnowing(file1=self.cpp1,file2=self.cpp2,lang="cpp")
        self.assertEqual(round(check.jaccardCheck(),2),0.38)
        self.assertEqual(round(check.plagiarismRate(),2),0.38)

    # testing for Java language
    def testForJava_Path(self):
        check = winnowing.Winnowing(file1= self.java1,file2=self.java2,lang="java")
        self.assertEqual(round(check.jaccardCheck(),2),1.00)
        self.assertEqual(round(check.plagiarismRate(),2),1.00)

    # testing with different type of files
    def testWithDifferentFiles(self):
        self.assertRaises(Exception,winnowing.Winnowing,file1=self.python1,file2=self.java1,lang="py")

    # testing with empty files
    def testWithEmptyFiles(self):
        self.assertRaises(Exception,winnowing.Winnowing,file1=self.emptyfile,file2=self.emptyfile,lang="r")
        
    # testing without passing language 
    def testWithoutPassingLanguage(self):
        self.assertRaises(Exception,winnowing.Winnowing,file1=self.python1,file2=self.python2)

    # testing with invalid arguments
    def testWithInvalidArguments(self):
        self.assertRaises(Exception,winnowing.Winnowing,rendom=self.python1,file2=self.python2,language="py")


    ''' Testing With Text of Files. '''
    def testForR_Code(self):
        file1 = open(self.r1,'r')
        file2 = open(self.r2,'r')
        code1 = file1.read()
        code2 = file2.read()
        file1.close()
        file2.close()
        check = winnowing.Winnowing(code1=code1,code2=code2,lang="r")
        self.assertEqual(round(check.jaccardCheck(),2),0.91)
        self.assertEqual(round(check.plagiarismRate(),2),0.91)

    def testForPython_Code(self):
        file1 = open(self.python1,'r')
        file2 = open(self.python2,'r')
        code1 = file1.read()
        code2 = file2.read()
        file1.close()
        file2.close()
        check = winnowing.Winnowing(code1=code1,code2=code2,lang="py")
        self.assertEqual(round(check.jaccardCheck(),2),0.57)
        self.assertEqual(round(check.plagiarismRate(),2),0.57)

    def testForCpp_Code(self):
        file1 = open(self.cpp1,'r')
        file2 = open(self.cpp2,'r')
        code1 = file1.read()
        code2 = file2.read()
        file1.close()
        file2.close()
        check = winnowing.Winnowing(code1=code1,code2=code2,lang="cpp")
        self.assertEqual(round(check.jaccardCheck(),2),0.38)
        self.assertEqual(round(check.plagiarismRate(),2),0.38)

    def testForJava_Code(self):
        file1 = open(self.java1,'r')
        file2 = open(self.java2,'r')
        code1 = file1.read()
        code2 = file2.read()
        file1.close()
        file2.close()
        check = winnowing.Winnowing(code1=code1,code2=code2,lang="java")
        self.assertEqual(round(check.jaccardCheck(),2),1.00)
        self.assertEqual(round(check.plagiarismRate(),2),1.00)
    
    def testWithEmptyCode1(self):
         self.assertRaises(Exception,winnowing.Winnowing,code1="",cpde2="",language="py")
    
    def testWithEmptyCode2(self):
         self.assertRaises(Exception,winnowing.Winnowing,code1="   ",cpde2="    ",language="py")

    def testWithInvalidCode(self):
         self.assertRaises(Exception,winnowing.Winnowing,code1="jkdkskfk",cpde2="jljflkfjdsdl",language="py")





if __name__ == '__main__':
    unittest.main()