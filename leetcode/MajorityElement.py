# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majority_element(nums: list) -> int:
    count = {}

    for i in nums:
        count[i] = 1 if i not in count else count[i] + 1
        if count[i] >= len(nums) / 2:
            return i