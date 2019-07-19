# Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.

# Input:
# The first line of input contains an integer T denoting the number of test cases. For each test case first line contains N(size of array). The subsequent line contains N-1 array elements.

# Output:
# Print the missing number in array.

# Constraints:
# 1 ≤ T ≤ 200
# 1 ≤ N ≤ 107
# 1 ≤ C[i] ≤ 107

# Example:
# Input:
# 2
# 5
# 1 2 3 5
# 10
# 1 2 3 4 5 6 7 8 10

# Output:
# 4
# 9

# Explanation:
# Testcase 1: Given array : 1 2 3 5. Missing element is 4


#code
def find_missing_element(arr_size, arr_list):
    sum_arr_list = 0
    sum_natural = (arr_size) * (arr_size +1)/2
    for y in arr_list:
        sum_arr_list += y
    return int(sum_natural - sum_arr_list)

test_cases = int(input())
list_of_all = []
for test in range(test_cases):
    arr_size = int(input())
    list_of_all.append(arr_size)
    x = list(map(int,input().split()))
    list_of_all.append(x)
for x in range(len(list_of_all)):
    # print(x)
    if (x % 2  != 0):
        continue
    else:
        array_size = list_of_all[x]
        array_list = list_of_all[x+1]
        print(find_missing_element(array_size, array_list))

    