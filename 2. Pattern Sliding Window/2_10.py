def stringAnagrams1(patternString, inputString):
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


def stringAnagrams(patternString, inputString):
    patternFreq={}
    for char in patternString:
        if char not in patternFreq:
            patternFreq[char]=0
        patternFreq[char]+=1
    start=0
    windowFreq={}
    anagramIndicesStartsAt=[]
    for end in range(len(inputString)):
        currentChar=inputString[end]
        if currentChar not in windowFreq:
            windowFreq[currentChar]=0
        windowFreq[currentChar]+=1
        if end>=len(patternString)-1:
            if windowFreq==patternFreq:
                anagramIndicesStartsAt.append(start)
            leftMostChar=inputString[start]
            windowFreq[leftMostChar]-=1
            if windowFreq[leftMostChar]==0:
                del windowFreq[leftMostChar]
            start+=1
    return anagramIndicesStartsAt


def main():
    print(stringAnagrams("pq","ppqp"))
    print(stringAnagrams("abc","abbcabc"))

    
main()
         