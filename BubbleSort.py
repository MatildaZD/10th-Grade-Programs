#sorting algorithms 
"""
List: 8,4,6,7,3,1,2
first two aren't in order so change those
4,8,6,7,3,1,2
loop from left to right:
	compare adjacent items
	if they are out of order:
		switch them 
One full pass: 4,6,7,3,1,2,8
	8 got moved to the end because it is last 
	after one pass the largest number will be at the end
	after two passes the second largest number will be at
	the second to last position
It will need to run n-1 times
this is known as the bubble sort 

"""
import numpy as np
from numpy import random

#bubble sort is an O(n^2) algorithm
#more precisly, it does (n-1)^2 comparisons
#run time is going to be a quadratic function of the input number

def bubbleSort(lst):
	k=1
	swaps = True 
	#runs until we have a pass with no swaps 
	while swaps:
		swaps = False

	#loop through indices 	
		for i in range(len(lst)-k):
			if lst[i] > lst[i+1]:
				temp = lst[i]
				lst[i] = lst[i+1]
				lst[i+1] = temp

				#there was a swap -list not sorted yet
				swaps = True
		k += 1
"""
Bubble Sort:
					Best Case			Worst Case 			Average Case 
Num Comparisons:	n-1					~ n^2/2
				
Num Swaps:			0
"""
		

#sorting 10,000 items take about 14 seconds 	
	
def main():

	x=np.arange(10000)
	bubbleSort(x)

if __name__ == "__main__":
	main()



