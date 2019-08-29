# Write a Python function frequency(l) that takes as input a list of integers and returns a pair of the form (minfreqlist,maxfreqlist) where
# minfreqlist is a list of numbers with minimum frequency in l, sorted in ascending order
# maxfreqlist is a list of numbers with maximum frequency in l, sorted in ascending
# For instance
# >>> frequency([13,12,11,13,14,13,7,11,13,14,12])
# ([7], [13])

# >>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14])
# ([7], [13, 14])

# >>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7])
# ([7, 11, 12], [13, 14])


def frequency(nums):
    pairs = {}
    minfreqlist = []
    maxfreqlist = []
    min, max = float("inf"), -1
    for i in range(len(nums)):
        pairs[nums[i]] = pairs.get(nums[i], 0) + 1
    for key, val in pairs.items():
        if val > max:
            max = val
        if val < min:
            min = val
    for key, val in pairs.items():
        if val == max:
            maxfreqlist.append(key)
        if val == min:
            minfreqlist.append(key)
    minfreqlist.sort()
    maxfreqlist.sort()
    return (minfreqlist, maxfreqlist)


print(frequency([4, 4, 4, 1, 1, 2, 2, 2, 3, 3]))
