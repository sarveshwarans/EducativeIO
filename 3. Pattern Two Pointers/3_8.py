def sortColors(nums):
    left=0 #anything left to this is all 0's
    right=len(nums)-1 # anything right to this is all 2's
    currentPointer=0 #initially all the numbers are uncategorized. As and when we process we will move the 0's to left and 1's to right
    while currentPointer<=right:#Important - we need to go only till we encounter 2 which is start of right index
        currentNumber=nums[currentPointer]
        if currentNumber==1:#this is middle number. We dont care about this. dont do anything
            currentPointer+=1
        elif currentNumber==0:
            #We need to swap places
            nums[currentPointer],nums[left]=nums[left],nums[currentPointer]
            currentPointer+=1
            left+=1
        elif currentNumber==2:
            nums[currentPointer],nums[right]=nums[right],nums[currentPointer]
            right-=1
            #We will not move the current pointer as we have anew element here and we need to process it
    return nums

def main():
    print(sortColors([1, 0, 2, 1, 0])) 
    print(sortColors([2, 2, 0, 1, 2, 0]))

main()
