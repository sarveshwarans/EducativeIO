def findWordsConcatenation1(givenWords,inputString):
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


def findWordsConcatenation(givenWords,inputString):
    givenWordFreq={}
    for word in givenWords:
        if word not in givenWordFreq:
            givenWordFreq[word]=0
        givenWordFreq[word]+=1
    start=0
    outputIndicesStartsAt=[]
    windowFreq={}
    for end in range(len(inputString)):
        if end>=len(givenWords[0]*len(givenWordFreq))-1:
            firstWord=inputString[start:start+len(givenWords[0])]
            lastWord=inputString[start+len(givenWords[0]):end+1]
            if firstWord not in windowFreq:
                windowFreq[firstWord]=0
            windowFreq[firstWord]+=1
            if lastWord not in windowFreq:
                windowFreq[lastWord]=0
            windowFreq[lastWord]+=1
            if windowFreq==givenWordFreq:
                outputIndicesStartsAt.append(start)
            windowFreq={}
            start+=1
    return outputIndicesStartsAt

def main():
    print(findWordsConcatenation(["cat","fox"],"catfoxcat"))
    print(findWordsConcatenation(["cat","fox"],"catcatfoxfox"))

    
main()
         
""" splitWord = [currentString[i:i+len(givenWords[0])] for i in range(0,len(currentString),len(givenWords[0]))]"""