def findWordsConcatenation(givenWords,inputString):
    givenWordsFreq={}
    for word in givenWords:
        if word not in givenWordsFreq:
            givenWordsFreq[word]=0
        givenWordsFreq[word]+=1
    windowStart = 0
    windowEnd = 0
    windowWordFreq={}
    outputIndices = []
    windowChar,firstHalf,secondHalf='','',''
    for windowEnd in range(len(inputString)):
        currentChar = inputString[windowEnd]
        windowChar += currentChar
        if windowEnd>=len(givenWords)*len(givenWords[0])-1:
            firstHalf = windowChar[:int(len(windowChar)/len(givenWords))]
            secondHalf =windowChar[int(len(windowChar)/len(givenWords)):]
            windowWordFreq[firstHalf]=1
            windowWordFreq[secondHalf]=1
            if givenWordsFreq==windowWordFreq:
                outputIndices.append(windowStart)
            windowStart+=1
            windowChar = windowChar[1:]
            firstHalf,secondHalf='',''
            windowWordFreq={}
    return outputIndices



def main():
    print(findWordsConcatenation(["cat","fox"],"catfoxcat"))
    print(findWordsConcatenation(["cat","fox"],"catcatfoxfox"))

    
main()
         