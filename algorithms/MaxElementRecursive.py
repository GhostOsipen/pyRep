def max_element_recursive(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]
    if nums[1] < nums[0]:
        nums[1], nums[0] = nums[0], nums[1]
    return max_element_recursive(nums[1:])