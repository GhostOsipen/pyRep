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

#print(my_binary_search([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,
#51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], 55))

print(my_binary_search([1,3,6], 2))
