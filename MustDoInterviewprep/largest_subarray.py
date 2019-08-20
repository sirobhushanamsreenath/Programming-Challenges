# Given an array of 0's and 1's your task is to complete the function maxLen which returns size of the largest sub array with equal number of 0's and 1's. The function maxLen takes 2 arguments. The first argument is the array A[] and second argument is the size 'N' of the array A[].

# Input:
# The first line of the input is T denoting the number of test cases. Then T test cases follow . Each test case contains two lines. The first line of each test case is a number N denoting the size of the array and in the next line are N space separated values of A [].

# Output:
# For each test case output in a new line the max length of the subarray.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 100
# 0 <= A[] <= 1

# Example:
# Input 
# 2
# 4
# 0 1 0 1
# 5
# 0 0 1 0 0

# Output
# 4
# 2

# Explanation:
# Testacase 1: The array from index [0...3] contains equal number of 0's and 1's. Thus maximum length of subarray having equal number of 0's and 1's is 4. 


#code
def maxLen(n, lis):
	dict = {0:0}
	result = 0
	for x in range(n):
		if lis[x] == 0:
			lis[x] = -1
	for x in range(n):
		for y in range(x+1,n+1,1):
			sum = 0
			arr1 = lis[x:y]
			for z in range(len(arr1)):
				sum += arr1[z]
			if ((sum == 0) and (dict[0] < z)):
				dict.update({0:z})
				result = z + 1
	return result

test_cases = int(input())
list_of_arr = []
for i in range(test_cases):
	arr_size = int(input())
	arr = list(map(int,input().split()))
	list_of_arr.append(arr)
for x in list_of_arr:
	print(maxLen(len(x),x))
