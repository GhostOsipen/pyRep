import math

def my_binary_search(nums: list, target: int) -> int:
    nums.sort()
    maxN = nums[-1]
    minN = nums[0]
    search = math.floor((maxN + minN) / 2)
    stepCount = 0

    if target < minN or target > maxN:
        return None
    else:
        while search != target:
            stepCount += 1
            search = math.floor((maxN + minN) / 2)
            if search > target:
                maxN = search
            if search < target:
                minN = search
        else:
            print('Number of elements %s' % len(nums))
            print('Steps to find %s.' % stepCount)
            return search
