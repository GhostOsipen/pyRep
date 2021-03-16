def my_binary_search(nums: list, target: int) -> int:
    high = len(nums) - 1
    low = 0

    if target < nums[0] or target > nums[-1]:
        return None
    while high >= low:
        mid = (high + low) // 2
        if target  <  nums[mid]:
            high = mid - 1
        elif target  >  nums[mid]:
            low = mid + 1
        else:
            return mid
    else:
        return None
