def sum_recursive(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]
    else:
        return nums.pop(0) + sum_recursive(nums)