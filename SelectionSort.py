"""
Selection Sort:

Loop N-1 Times
	Loop through unsorted part of list
		find minimum
		swap unsorted list 

"""

import numpy as np
from numpy import random

lst = [8,9,3,5,2,4,1]

def selectionSort(lst):
	for i in range(len(lst)-1):
		smallest = i 
		for j in range(i+1, len(lst)): 
			if lst[smallest] > lst[j]: 
				smallest = j 
				temp = lst[i]
		lst[i] = lst[smallest]
		lst[smallest] = temp

"""
On My computer: 
100 items:
Bubble: 0.749 Seconds
Selection: 0.280 Seconds

1000 items:
Bubble: 1.055 Seconds
Selection: .531 Seconds

10000 items: 
Bubble: 43.551 Seconds
Selection: 24.6 Seconds

Sorted List (of 10000)
Bubble: 1.005 Seconds
Selection: .668 Seconds

				Worst Case			
numComparisons	N^2/2 = O(n^2)  
				*same as bubble
num swaps		n-1 = O(n)

"""
def main():
	x=np.arange(10000)
	selectionSort(x)

if __name__ == "__main__":
	main()