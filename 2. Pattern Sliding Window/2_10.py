def stringAnagrams(patternString, inputString):
    windowStart = 0
    windowEnd = 0 
    startingIndicesOutput = []
    windowFrequency = {}
    patternFrequency = {}
    for character in patternString:
        if character not in patternFrequency:
            patternFrequency[character]=0
        patternFrequency[character]+=1
    patternLength = len(patternString)
    for windowEnd in range(len(inputString)):
        currentCharacter = inputString[windowEnd]
        if currentCharacter not in windowFrequency:
            windowFrequency[currentCharacter]=0
        windowFrequency[currentCharacter]+=1
        if windowEnd>=patternLength-1:
            if windowFrequency == patternFrequency:
                startingIndicesOutput.append(windowStart)
            leftChar = inputString[windowStart]
            windowFrequency[leftChar]-=1
            if windowFrequency[leftChar]==0:
                del windowFrequency[leftChar]
            windowStart+=1
    return startingIndicesOutput

def main():
    print(stringAnagrams("pq","ppqp"))
    print(stringAnagrams("abc","abbcabc"))

    
main()
         