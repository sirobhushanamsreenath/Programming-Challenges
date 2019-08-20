# Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

# Output:
# For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 107
# 1 <= Ai <= 1010

# Example:
# Input:
# 2
# 5 12
# 1 2 3 7 5
# 10 15
# 1 2 3 4 5 6 7 8 9 10
# Output:
# 2 4
# 1 5

# Explanation : 
# Testcase1: sum of elements from 2nd position to 4th position is 12
# Testcase2: sum of elements from 1st position to 5th position is 15

#code
def find_subarray_sum(sum, list, size):
	# i=0
	# j=0
	# local_sum=arr[i]
	# if size==1:
	# 	return 0,0
	# while j+1<size and i<=j:
	# 	# print(local_sum,i,j)
	# 	if local_sum==sum:
	# 		# print(i+1,j+1)
	# 		return (print(i+1,j+1))
	# 	if local_sum+arr[j+1]<=sum:
	# 		local_sum+=arr[j+1]
	# 		j+=1
	# 	elif local_sum+arr[j+1]>=sum:
	# 		local_sum-=arr[i]
	# 		i+=1
		
	# return (print(-1))
	
	for x in range(len(list)):
		for y in range(x+1,len(list)+1,1): 
			final_sum = 0
			arr1 = list[x:y]
			# print('x : '+str(x)+' y : '+str(y)+' = '+str(list[x:y]))
			for z in arr1:
				final_sum += z
			if final_sum == sum:
				return(print(x+1,y))
	return (print(-1))


test_cases = int(input())
list_of_size = []
list_of_sum = []
list_of_arr = []
list_of_result = []
for x in range(test_cases):
	arr_sum=(list(map(int,input().split())))
	array = list(map(int,input().split()))
	list_of_size.append(arr_sum[0])
	list_of_sum.append(arr_sum[1])
	list_of_arr.append(array)
for x in range(len(list_of_sum)):
	find_subarray_sum(list_of_sum[x],list_of_arr[x],list_of_size[x])
# 	arr_sum = list(map(int,input().split()))
# 	list_of_sum.append(arr_sum[1])
# 	arr = list(map(int,input().split()))
# 	list_of_arr.append(arr)
# for x in range(len(list_of_arr)):
	# 

