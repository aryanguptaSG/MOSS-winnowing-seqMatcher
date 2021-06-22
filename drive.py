import winnowing


#Driver Code For Winnowing.py
check1 = winnowing.winnowing("/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test2.py","/Users/aryangupta/Desktop/IIT_Bombay/MOSS-winnowing-seqMatcher/tests/test3.py")
result=check1.jaccardCheck()
result1 = check1.plagiarismRate()
print("Approx ratio jaccard of plagiarized content in file 1: ", result['ratio'])
print("Approx ratio of plagiarized content in file 1: ", result1['ratio'])
# print(result['Code'])

