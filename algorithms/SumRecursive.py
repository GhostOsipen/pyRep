def sum_recursive(nums: list) -> int:
    return nums[0] if len(nums) == 1 else nums[0] + sum_recursive(nums[1:])