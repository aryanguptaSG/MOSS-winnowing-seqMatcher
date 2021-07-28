import hashlib
from cleanUP import tokenize,toText
import pygments.lexers
from os import path

class Winnowing():
    def __init__(self, file1=None, file2=None,code1=None,code2=None,lang=None):
        if file1 and file2:
            if not lang:
                raise Exception("Language required")
            self.text1 , self.text2  = self.checkPoint(file1,file2)
            lexer =pygments.lexers.get_lexer_by_name(lang)
            self.token1 = tokenize(text= self.text1,lexer=lexer)
            self.str1 = toText(self.token1)
            self.token2 = tokenize(text= self.text2,lexer=lexer)
            self.str2 = toText(self.token2)

        elif code1 and code2:
            if not lang:
                raise Exception("Language required")

            if len(code1.strip())<=0 or len(code2.strip())<=0:
                raise Exception("Code can not be empty!")

            self.text1=code1
            self.text2=code2
            lexer =pygments.lexers.get_lexer_by_name(lang)
            self.token1 = tokenize(text= self.text1,lexer=lexer)
            self.str1 = toText(self.token1)
            self.token2 = tokenize(text= self.text2,lexer=lexer)
            self.str2 = toText(self.token2)

        else:
            raise Exception("Invalid Arguments")

        self.kGrams1 = self.kgrams(self.str1)  #stores k-grams, their hash values and positions in cleaned up text
        self.kGrams2 = self.kgrams(self.str2)
        self.HL1 = self.hashList(self.kGrams1)  #hash list derived from k-grams list
        self.HL2 = self.hashList(self.kGrams2)
        self.fpList1 = self.fingerprints(self.HL1)
        self.fpList2 = self.fingerprints(self.HL2)
        

    def jaccardCheck(self):
        fp1 = set(self.fpList1)
        fp2 = set(self.fpList2)
        comman = fp1.intersection(fp2)
        total = len(fp1)+len(fp2)
        plagcount = len(comman)
        return (plagcount/(total-plagcount))
        
            
    def plagiarismRate(self):
        fp1 = set(self.fpList1)
        fp2 = set(self.fpList2)
        total = len(fp1)
        plagcount = len(fp1.intersection(fp2))
        return (plagcount/total)

    #we form windows of hash values and use min-hash to limit the number of fingerprints
    def fingerprints(self,arr, winSize = 4):
        arrLen = len(arr)
        prevMin = 0
        currMin = 0
        fingerprintList = []
        for i in range(arrLen - winSize):
            win = arr[i: i + winSize]  #forming windows
            currMin = i + self.minIndex(win)
            if not currMin == prevMin:  #min value of window is stored only if it is not the same as min value of prev window
                fingerprintList.append(arr[currMin])  #reduces the number of fingerprints while maintaining guarantee
                prevMin = currMin  #refer to density of winnowing and guarantee threshold (Stanford paper)

        return fingerprintList
        
    #takes k-gram list as input and returns a list of only hash values
    def hashList(self,arr):
        if not (len(arr)):
            raise Exception("Code is Invalid")
        return list(zip(*arr))[1]
        
    #function to form k-grams out of the cleaned up text
    def kgrams(self,text, k = 25):
        tokenList = list(text)
        n = len(tokenList)
        kgrams = []
        for i in range(n - k + 1):
            kgram = ''.join(tokenList[i : i + k])
            hv = self.hash(kgram)
            kgrams.append((kgram, hv, i, i + k))  #k-gram, its hash value, starting and ending positions are stored
            #these help in marking the plagiarized content in the original code.
        return kgrams

    #function that returns the index at which minimum value of a given list (window) is located
    def minIndex(self,arr):
        return arr.index(min(arr))

    #sha-1 encoding is used to generate hash values
    def hash(self,text):
        #this function generates hash values
        return int((hashlib.sha1(text.encode('utf-8'))).hexdigest()[-4:],16)#using last 16 bits of sha-1 digest

    def checkPoint(self,file1,file2):
        extension1 = path.splitext(file1)[1]
        extension2= path.splitext(file2)[1]
        if extension1!=extension2:
            raise Exception("Files should be of same type!")
        file = open(file1, "r")
        text1 = file.read()
        file.close()
        file = open(file2, "r")
        text2 = file.read()
        file.close()
        if len(text1)<=0 or len(text2)<=0:
            raise Exception("File Can not be empty!")
        return (text1,text2)

        



