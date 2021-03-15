def my_binary_search(nums: list, target: int) -> int:
    nums.sort()
    maxN = len(nums) - 1
    minN = 0
    mid = maxN

    if target < nums[minN] or target > nums[maxN]:
        return None
    else:
        while nums[mid] != target:
            mid = (maxN + minN) // 2
            if target  >  nums[mid]:
                minN = mid
            elif target  <  nums[mid]:
                maxN = mid
        else:
            print('Number of elements %s' % len(nums))
            return mid
            
            

print(my_binary_search([1, 3, 6], 2))