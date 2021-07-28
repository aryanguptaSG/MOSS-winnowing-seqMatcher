import winnowing


#Driver Code For Winnowing.py
check = winnowing.Winnowing(file1= "/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test8.java",file2="/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test9.java",lang="r")

# code1 = open("/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test6.r",'r').read()
# code2 = open("/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test7.r",'r').read()

# check = winnowing.Winnowing(code1=code1,code2=code2,lang="r")


result=check.jaccardCheck()
result1 = check.plagiarismRate()
print("Approx ratio jaccard of plagiarized content in file 1: ", result)
print("Approx ratio of plagiarized content in file 1: ", result1)


