import random

def quick_sort(nums: list) -> list:
    if nums == []:
        return nums

    low = []
    high = []
    main = nums.pop(random.randrange(len(nums)))

    for i in nums:
        low.append(i) if i < main else high.append(i)

    return quick_sort(low) + [main] + quick_sort(high) 