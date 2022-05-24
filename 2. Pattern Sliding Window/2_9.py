def permutationInString(patternString, inputString):
    windowStart = 0
    windowEnd = 0 
    patternFrequency = {}
    windowFrequency = {}
    patternLength = len(patternString)
    for character in patternString:
        if character not in patternFrequency:
            patternFrequency[character]= 0
        patternFrequency[character]+=1
    for windowEnd in range(len(inputString)):
        currentChar = inputString[windowEnd]
        if currentChar not in windowFrequency:
            windowFrequency[currentChar] = 0
        windowFrequency[currentChar] += 1
        if windowEnd >= patternLength-1:
            if windowFrequency == patternFrequency:
                return True
            else:
                leftChar = inputString[windowStart]
                windowFrequency[leftChar] -=1
                if windowFrequency[leftChar]==0:
                    del windowFrequency[leftChar]
                windowStart += 1
    return False

def main():
    print(permutationInString("abc","oidbcaf"))
    print(permutationInString("dc","odicf"))
    print(permutationInString("bcdyabcdx","bcdxabcdy"))
    print(permutationInString("abc","aaacb"))
    
main()
            