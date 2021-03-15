def my_binary_search(nums: list, target: int) -> int:
    nums.sort()
    maxN = len(nums) - 1
    minN = 0

    if target < nums[minN] or target > nums[maxN]:
        return None
    else:
        while nums[(maxN + minN) // 2] != target:
            if (maxN-minN) == 1:
                return None
            else:
                if nums[(maxN + minN) // 2] > target:
                    maxN = (maxN + minN) // 2
                elif nums[(maxN + minN) // 2] < target:
                    minN = (maxN + minN) // 2
        else:
            print('Number of elements %s' % len(nums))
            return (maxN + minN) // 2
