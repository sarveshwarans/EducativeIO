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

def findSmallestWindowContainingSubstring(patternString,inputString):
    windowStart = 0
    windowEnd = 0
    smallestSubstring = ''
    wantFreq = {}
    wantFreqCount = 0
    haveFreq ={}
    haveFreqCount = 0
    for character in patternString:
        if character not in wantFreq:
            wantFreq[character]=0
        wantFreq[character]+=1
    wantFreqCount=len(wantFreq)
    for windowEnd in range(len(inputString)):
        currentChar=inputString[windowEnd]
        if currentChar in patternString:
            if currentChar not in haveFreq:
                haveFreq[currentChar]=0
            haveFreq[currentChar]+=1
            if haveFreq[currentChar]==wantFreq[currentChar]:
                haveFreqCount+=1
        while haveFreqCount>=wantFreqCount:
            smallestSubstring = inputString[windowStart:windowEnd+1]
            leftChar=inputString[windowStart]
            if leftChar in patternString:
                haveFreq[leftChar]-=1
                if haveFreq[leftChar]<wantFreq[leftChar]:
                    haveFreqCount-=1
                if haveFreq[leftChar]==0:
                    del haveFreq[leftChar]
            windowStart+=1
    return smallestSubstring






def main():
    print(findSmallestWindowContainingSubstring("ABC","ADOBECODEBANC"))
    print(findSmallestWindowContainingSubstring("abc","adcad"))
    print(findSmallestWindowContainingSubstring("aba","bbaa"))

    
main()
         
        

