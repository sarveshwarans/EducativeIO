from collections import deque


def productLessThanTarget(k,nums):
    left=0
    currentProduct=1
    count=0
    outputList=[]
    """the numbers should be in same order. So lets keep multiplying the nums in same order till we get the product>=k
    Now that the number is >k let us start incrementing left and check if the new product>=k
    Whenever we move the left pointer we need to divide the product by left number
    everytime we process a right pointer, we add it to the output(deque)
    after figuring the right and left, we can use deque to add the combinations
    https://leetcode.com/problems/subarray-product-less-than-k/discuss/560093/Python3-two-pointer-O(N)-O(1)-with-breakdown
    """
    for right in range(len(nums)):
        currentProduct*=nums[right]
        while currentProduct>=k:
            currentProduct/=nums[left]
            left+=1
        count+=right-left+1
        tempList=deque()
        for right in range(right,left-1,-1):
            tempList.appendleft(nums[right])
            outputList.append(list(tempList))
    return outputList


def main():
    print(productLessThanTarget(30,[2, 5, 3, 10]))
    print(productLessThanTarget(100,[10,5,2,6]))  

main()

"""
2 5 3 10 -> 2 5 25 3 53 10
8 2 6 5 -> 8 2 82 6 26 5 65
"""