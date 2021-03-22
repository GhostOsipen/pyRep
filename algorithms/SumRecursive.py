def sum_recursive(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]
    else:
        return nums.pop(0) + sum_recursive(nums)

def sum_recursive1(nums: list) -> int:
    return nums[0] if len(nums) == 1 else sum_recursive(nums[0:])

print(sum_recursive1([1,3,6,5]))