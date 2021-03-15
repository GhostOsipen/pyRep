def my_binary_search(nums: list, target: int) -> int:
    nums.sort()
    maxN = len(nums) - 1
    minN = 0
    mid = maxN

    if target < nums[minN] or target > nums[maxN]:
        return None
    else:
        while nums[mid] != target:
            if (maxN-minN) == 1:
                return None
            else:
                if nums[mid] > target:
                    maxN = mid
                elif nums[mid] < target:
                    minN = mid
                mid = (maxN + minN) // 2
        else:
            print('Number of elements %s' % len(nums))
            return mid
