import winnowing


#Driver Code For Winnowing.py
check = winnowing.Winnowing("/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test3.py","/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test3.py")
result=check.jaccardCheck()
result1 = check.plagiarismRate()
# result3 = check.plagiarismCheck()
print("Approx ratio jaccard of plagiarized content in file 1: ", result['ratio'])
print("Approx ratio of plagiarized content in file 1: ", result1['ratio'])
# print("plagiarized content in file 1: ", result3['ratio'])
# print(result3['Code'])


#  python , c, c++, java, R 

# minimum two files for each language. (empty files as well.)

