def two_sum(nums, totalsum):
    left = 0
    right = len(nums) - 1
    while left < right:
        currentSum = nums[left] + nums[right]
        if currentSum == totalsum:
            return [nums[left], nums[right]]
        elif currentSum < totalsum:
            left += 1
        elif currentSum > totalsum:
            right -= 1
    return[]


print(two_sum([1, 2, 3, 4], 3))
