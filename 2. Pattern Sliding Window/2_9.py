def permutationInString(patternString, inputString):
    patternLength = len(patternString)
    windowStart = 0
    windowEnd = 0
    patternFreq = {}
    for character in patternString:
        if character not in patternFreq:
            patternFreq[character]=0
        patternFreq[character]+=1
    windowFreq={}
    for windowEnd in range(len(inputString)):
        currentChar=inputString[windowEnd]
        if currentChar not in windowFreq:
            windowFreq[currentChar]=0
        windowFreq[currentChar]+=1
        if windowEnd>=patternLength-1:
            if windowFreq==patternFreq:
                return True
            leftChar=inputString[windowStart]
            windowFreq[leftChar]-=1
            if windowFreq[leftChar]==0:
                del windowFreq[leftChar]
            windowStart+=1
    return False

def main():
    print(permutationInString("abc","oidbcaf"))
    print(permutationInString("dc","odicf"))
    print(permutationInString("bcdyabcdx","bcdxabcdy"))
    print(permutationInString("abc","aaacb"))
    
main()
            