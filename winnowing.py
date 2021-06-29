import hashlib
from cleanUP import tokenize,toText

class Winnowing():
    def __init__(self, file1, file2):
        self.file1=file1
        self.file2=file2
        self.token1 = tokenize(file1)  #from cleanUP.py
        self.str1 = toText(self.token1)
        self.token2 = tokenize(file2)
        self.str2 = toText(self.token2)
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
        return {"ratio":(plagcount/(total-plagcount))}
        
            
    def plagiarismRate(self):
        fp1 = set(self.fpList1)
        fp2 = set(self.fpList2)
        total = len(fp1)
        plagcount = len(fp1.intersection(fp2))
        return {"ratio":(plagcount/total)}

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



