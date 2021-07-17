import unittest
import winnowing


class TestWinnowing(unittest.TestCase):
    # testing for R language
    def test1(self):
        check = winnowing.Winnowing(file1= "/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test6.r",file2="/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test7.r",lang="r")
        self.assertEqual(check.jaccardCheck(),0.9130434782608695)
        self.assertEqual(check.plagiarismRate(),0.9130434782608695)

    # testing for Python language
    def test2(self):
        check = winnowing.Winnowing(file1= "/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test2.py",file2="/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test3.py",lang="py")
        self.assertEqual(check.jaccardCheck(),0.5669642857142857)
        self.assertEqual(check.plagiarismRate(),0.5669642857142857)
    
    # testing for C++ language
    def test3(self):
        check = winnowing.Winnowing(file1= "/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test4.cpp",file2="/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test5.cpp",lang="cpp")
        self.assertEqual(check.jaccardCheck(),0.5666666666666667)
        self.assertEqual(check.plagiarismRate(),0.5666666666666667)

    # testing for Java language
    def test4(self):
        check = winnowing.Winnowing(file1= "/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test8.java",file2="/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test9.java",lang="r")
        self.assertEqual(check.jaccardCheck(),1.0)
        self.assertEqual(check.plagiarismRate(),1.0)

    # testing with different type of files
    def test5(self):
        self.assertRaises(Exception,winnowing.Winnowing,file1="/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test2.py",file2="/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test8.java",lang="py")

    # testing with empty files
    def test6(self):
        self.assertRaises(Exception,winnowing.Winnowing,file1="/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test1.txt",file2="/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test1.txt",lang="r")
        
    # testing without passing language 
    def test6(self):
        self.assertRaises(Exception,winnowing.Winnowing,file1="/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test2.py",file2="/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test3.py")

    # testing with invalid arguments
    def test7(self):
        self.assertRaises(Exception,winnowing.Winnowing,rendom="/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test2.py",file2="/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test3.py",language="py")



if __name__ == '__main__':
    unittest.main()