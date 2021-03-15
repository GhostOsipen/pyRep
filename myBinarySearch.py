def my_binary_search(nums: list, target: int) -> int:
    nums.sort()
    maxN = len(nums) - 1
    minN = 0
    mid = (maxN + minN) // 2

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

print(my_binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 3))
