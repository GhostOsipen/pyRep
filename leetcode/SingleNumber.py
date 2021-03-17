# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Follow up: Could you implement a solution with a linear runtime complexity 
# and without using extra memory?

def singleNumber(nums: list) -> int:
    B = []
    C = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i<j:
                B.append(nums[i])
    for i in nums:
        if not (i in B):
            C.append(i)
    return C[0]

def singleNumber2(nums: list) -> int:
    count = {}
    for i in nums:
        count[i] = 1 if i not in count else count[i] + 1
    for i in count:
        if count[i] == 1:
            return i
    return -1

print(singleNumber2([4,1,4,5,2,1,2]))
