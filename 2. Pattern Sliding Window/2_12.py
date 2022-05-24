def findWordsConcatenation(givenWords,inputString):
    windowStart = 0
    windowEnd = 0
    currentWord = ""
    givenWordFreq = {}
    givenWordLength = len(givenWords[0])
    givenWordsTotalLength = 0
    for word in givenWords:
        if word not in givenWordFreq:
            givenWordsTotalLength += len(word)
            givenWordFreq[word]=0
        givenWordFreq[word]+=1
    windowFreq = {}
    startingIndicesOutput = []

    for windowEnd in range(len(inputString)):
        currentChar = inputString[windowEnd]
        currentWord += currentChar 
        if windowEnd>=givenWordsTotalLength-1:
            windowWordsSplit = [currentWord[i:i+givenWordLength] for i in range(0,len(currentWord),givenWordLength)]
            for word in windowWordsSplit:
                if word not in windowFreq:
                    windowFreq[word]=0
                windowFreq[word]+=1
            if windowFreq == givenWordFreq:
                startingIndicesOutput.append(windowStart)
                for word in windowFreq:
                    windowFreq[word]-=1
            windowStart+=1
            currentWord = currentWord[1:]
            windowFreq = {}
    return startingIndicesOutput


def main():
    print(findWordsConcatenation(["cat","fox"],"catfoxcat"))
    print(findWordsConcatenation(["cat","fox"],"catcatfoxfox"))

    
main()
         