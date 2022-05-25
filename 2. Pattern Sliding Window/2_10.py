def stringAnagrams(patternString, inputString):
    windowStart = 0
    windowEnd = 0
    patternFreq = {}
    for character in patternString:
        if character not in patternFreq:
            patternFreq[character]=0
        patternFreq[character]+=1
    windowFreq = {}
    outputIndicesList = []
    for windowEnd in range(len(inputString)):
        currentChar=inputString[windowEnd]
        if currentChar not in windowFreq:
            windowFreq[currentChar]=0
        windowFreq[currentChar]+=1
        if windowEnd>=len(patternString)-1:
            if windowFreq==patternFreq:
                outputIndicesList.append(windowStart)
            leftChar=inputString[windowStart]
            windowFreq[leftChar]-=1
            if windowFreq[leftChar]==0:
                del windowFreq[leftChar]
            windowStart+=1
    return outputIndicesList

def main():
    print(stringAnagrams("pq","ppqp"))
    print(stringAnagrams("abc","abbcabc"))

    
main()
         