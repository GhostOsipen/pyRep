def my_binary_search(nums: list, target: int) -> int:
    nums.sort()
    maxN = len(nums) - 1
    minN = 0
    mid = maxN

    if target < nums[minN] or target > nums[maxN]:
        return None
    else:
        while maxN >= minN:
            if target != nums[mid]:
                mid = (maxN + minN) // 2
                if target  <  nums[mid]:
                    maxN = mid - 1
                elif target  >  nums[mid]:
                    minN = mid + 1
            else:
                print('Number of elements %s' % len(nums))
                return mid
        else:
            return None
