# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majority_element(nums: list) -> int:
    last: int = None
    nums.sort()
    
    for i in nums:
        if last != i:
            if nums.count(i) > (len(nums)/2):
                return i
        last = i        
     
print(majority_element([2,2,1,1,1,2,2]))