from sys import path
import sys

"""windowStart = 0
windowEnd = 0

haveCount = 0
windowFrequency = {}
patternFrequence = {}
subString = ""
subStringLength = sys.maxsize
for character in patternString:
    if character not in patternFrequence:
        patternFrequence[character]=0
        windowFrequency[character]=0
    patternFrequence[character]+=1
needCount = len(patternFrequence)


for windowEnd in range(len(inputString)):
    currentChar = inputString[windowEnd]
    if currentChar in patternString:
        windowFrequency[currentChar]+=1
        if windowFrequency[currentChar]==patternFrequence[currentChar]:
            haveCount += 1
    if haveCount == len(patternFrequence):

        while haveCount==len(patternString):
            if len(inputString[windowStart:windowEnd+1]) < subStringLength:
                subStringLength = len(inputString[windowStart:windowEnd+1])
                subString = inputString[windowStart:windowEnd+1]
            leftChar = inputString[windowStart]
            
            if leftChar in patternString:
                windowFrequency[leftChar]-=1
                if windowFrequency[leftChar]>=patternFrequence[leftChar]:
                    pass
                else:
                    haveCount -=1
            windowStart+=1
if subString == "" and patternString == inputString:
    subString = inputString        
return subString"""

def findSmallestWindowContainingSubstring1(patternString,inputString):
    windowStart = 0
    windowEnd = 0 
    needCount = 0
    haveCount = 0
    patternFreq = {}
    outputStringLength = sys.maxsize
    outputString = ""


    for character in patternString:
        if character not in patternFreq:
            patternFreq[character] = 0
        patternFreq[character]+=1
        #needCount +=1 
    needCount = len(patternFreq)
    windowFreq = {}
    
    for windowEnd in range(len(inputString)):
        currentChar = inputString[windowEnd]
        if currentChar in patternString:
            if currentChar not in windowFreq:
                windowFreq[currentChar]=0
            windowFreq[currentChar]+=1
            if windowFreq[currentChar] == patternFreq[currentChar]:
                haveCount += 1

        while haveCount == needCount:
            if windowEnd-windowStart+1 < outputStringLength:
                outputStringLength = windowEnd-windowStart+1
                outputString = inputString[windowStart:windowEnd+1]
            leftChar = inputString[windowStart]
            if leftChar in patternString:
                windowFreq[leftChar]-=1
                if windowFreq[leftChar] < patternFreq[leftChar]:
                    haveCount -=1
            windowStart+=1
    return outputString


def findSmallestWindowContainingSubstring(patternString,inputString):
    patternFreq={}
    wantCount=0
    for char in patternString:
        if char not in patternFreq:
            patternFreq[char]=0
        patternFreq[char]+=1
        wantCount+=1
    windowFreq={}
    start=0
    haveCount=0
    outputString=""
    outputLength=sys.maxsize
    for end in range(len(inputString)):
        currentChar=inputString[end]
        if currentChar in patternString:
            if currentChar not in windowFreq:
                windowFreq[currentChar]=0
            windowFreq[currentChar]+=1
            if windowFreq[currentChar]<=patternFreq[currentChar]:
                haveCount+=1
            while haveCount>=wantCount:
                currentLength=end-start+1
                if outputLength>currentLength:
                    outputString=inputString[start:end+1]
                    outputLength=len(outputString)
                leftMostChar=inputString[start]
                if leftMostChar in patternString:
                    windowFreq[leftMostChar]-=1
                    if windowFreq[leftMostChar]<patternFreq[leftMostChar]:
                        haveCount-=1
                    if windowFreq[leftMostChar]==0:
                        del windowFreq[leftMostChar]
                start+=1  
    return outputString



def main():
    print(findSmallestWindowContainingSubstring("ABC","ADOBECODEBANC"))
    print(findSmallestWindowContainingSubstring("abc","adcad"))
    print(findSmallestWindowContainingSubstring("aba","bbaa"))
    print(findSmallestWindowContainingSubstring("abc","aabdec"))
    
main()
         
        

