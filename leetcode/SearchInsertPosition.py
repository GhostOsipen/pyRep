# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

def searchInsert(nums: list, target: int) -> int:
    pos = 0
    if target in nums:
        return nums.index(target)
    else:
        for i in nums:
            if target < i:
                pos = nums.index(i)
                break
            else:
                pos += 1
        return pos


print(searchInsert([1, 3, 5, 6], 5))
