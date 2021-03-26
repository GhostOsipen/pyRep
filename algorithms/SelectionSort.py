def my_selection_sort(nums: list) -> list:
    sortedNums = []

    def smallest_element(nums: list) -> int:
        minN = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < minN:
                minN = nums[i]
        return minN

    while len(nums) > 0:
        sortedNums.append(nums.pop(nums.index(smallest_element(nums))))

    return sortedNums            