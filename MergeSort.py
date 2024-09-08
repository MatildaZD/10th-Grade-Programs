

def merge(left, right):
	i1 = 0 #index into the left list
	i2 = 0 #index into the right list
	newList = []
	while i1 < len(left) or i2 < len(right):
		if i1 >= len(left):
			newList.append(right[i2])
			i2 += 1
		elif i2 >= len(right):
			newList.append(left[i1]) #append item from left
			i1 += 1			
		elif left[i1] <= right[i2]: #if item in left is smaller
			newList.append(left[i1]) #append item from left
			i1 += 1
		elif right[i2] < left[i1]:
			newList.append(right[i2])
			i2 += 1
	return newList

#O(n) recursive calls
#Each takes O(n)
#overall O(n^2)



def mergeSort(lst):
	n = len(lst)
	if n <= 1:
		return lst
	#sort the left half
	left = mergeSort(lst[:n//2])
	#sort the right half
	right = mergeSort(lst[n//2:])
	#merge them together
	return merge(left, right)

import numpy as np
from numpy import random

def main():
	x=np.random.rand(3500000)
	list(x)
	mergeSort(x)

if __name__ == "__main__":
	main()
