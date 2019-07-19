# Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.

# Input:  
# The first line of the input contains T denoting the number of testcases. The first line of the test case will be the size of array and second line will be the elements of the array.

# Output: 
# For each test case the output will be the majority element of the array. Output "-1" if no majority element is there in the array.

# Constraints:
# 1 <= T<= 100
# 1 <= N <= 107
# 0 <= Ai <= 106

# Example:
# Input:
# 2
# 5
# 3 1 3 3 2
# 3
# 1 2 3

# Output:
# 3
# -1

# Explanation:
# Testcase 1: Since, 3 is present more than N/2 times, so it is the majority element.

#code
def find_majority_element(array_list):
	majority_count = int(len(array_list)/2)
	max_count_element = -1
	dictionary = {}
	for x in array_list:
		dictionary[x] = dictionary.get(x,0) + 1
		if dictionary[x] > majority_count:
			max_count_element = x
	return max_count_element

test_cases = int(input())
list_of_all = []
for x in range(test_cases):
	arr_size = int(input())
	array = list(map(int,input().split()))
	list_of_all.append(array)
for y in range(len(list_of_all)):
	print(find_majority_element(list_of_all[y]))