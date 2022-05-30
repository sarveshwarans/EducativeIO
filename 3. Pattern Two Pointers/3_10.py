from collections import deque


def stringContainingBackspaces(str1,str2):
    leftCorrectedString=deque()
    rightCorrectedString=deque()

    rightPointer=len(str1)-1
    leftPointer=0
    hashCount=0
    while rightPointer>=leftPointer:
        currentCharOfLeftString=str1[rightPointer]
        if currentCharOfLeftString!='#':
            leftCorrectedString.appendleft(currentCharOfLeftString)
            rightPointer-=1
        else:
            hashPointer=rightPointer
            while hashPointer>leftPointer and currentCharOfLeftString=='#':
                hashCount+=1
                hashPointer-=1
                currentCharOfLeftString=str1[hashPointer]
            rightPointer-=2*hashCount
        hashCount=0

    
    rightPointer=len(str2)-1
    leftPointer=0
    hashCount=0
    while rightPointer>=leftPointer:
        currentCharOfRightString=str2[rightPointer]
        if currentCharOfRightString!='#':
            rightCorrectedString.appendleft(currentCharOfRightString)
            rightPointer-=1
        else:
            hashPointer=rightPointer
            while hashPointer>leftPointer and currentCharOfRightString=='#':
                hashCount+=1
                hashPointer-=1
                currentCharOfRightString=str2[hashPointer]
            rightPointer-=2*hashCount
        hashCount=0
    if leftCorrectedString==rightCorrectedString:
        return True
    else:
        return False
    

def main():
    print(stringContainingBackspaces("xy#z","xzz#")) 
    print(stringContainingBackspaces("xy#z","xyz#")) 
    print(stringContainingBackspaces("xp#","xyz##")) 
    print(stringContainingBackspaces("xywrrmp","xywrrmu#p")) 
main()
