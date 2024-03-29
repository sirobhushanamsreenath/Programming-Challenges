# Write a function accordian(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements alternates between increasing strictly and decreasing strictly.

# Here are some examples of how your function should work.


#   >>> accordian([1,5,1])
#   False
# Explanation: Differences between adjacent elements are 5-1 = 4, 5-1 = 4, which are equal.


#   >>> accordian([1,5,2,8,3])
#   True
# Explanation: Differences between adjacent elements are 5-1 = 4, 5-2 = 3, 8-2 = 6, 8-3 = 5, so the differences decrease, increase and then decrease.


#   >>> accordian([-2,1,5,2,8,3])
#   True
# Explanation: Differences between adjacent elements are 1-(-2) = 3, 5-1 = 4, 5-2 = 3, 8-2 = 6, 8-3 = 5, so the differences increase, decrease, increase and then decrease.


#   >>> accordian([1,5,2,8,1])
#   False
# Explanation: Differences between adjacent elements are 1-(-2) = 3, 5-1 = 4, 5-2 = 3, 8-2 = 6, 8-1 = 7, so the differences increase, decrease, increase and then increase again.

def accordian(l):
    prevdiff = abs(l[0] - l[1])
    diff = abs(l[1] - l[2])
    increase, decrease = 0, 0
    if diff > prevdiff:
        increase, decrease = 1, 0
    elif diff < prevdiff:
        increase, decrease = 0, 1
    else:
        return False
    for i in range(2, len(l) - 1):
        prevdiff = diff
        diff = abs(l[i] - l[i + 1])
        if diff > prevdiff and decrease == 1:
            increase, decrease = 1, 0
        elif diff < prevdiff and increase == 1:
            increase, decrease = 0, 1
        else:
            return False
    return True


print(accordian([1, 5, 1]))
print(accordian([1, 5, 2, 8, 3]))
print(accordian([-2, 1, 5, 2, 8, 3]))
print(accordian([1, 5, 2, 8, 1]))
