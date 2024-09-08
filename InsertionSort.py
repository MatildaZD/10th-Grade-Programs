"""
Pseudo Code:

if it is less than the value before it, switch the indices
continue until the item before it is less than the item currently
beingfor each item in the list, compare it to the item before it, then
 compared 

Loop each index from position 1 onward: 
	save number at index in a variable 
	loop backwards from index-1 until you find item
	<number:
		shift item 1 spot right

	insert number at correct position

"""
import numpy as np
from numpy import random


def insertionSort(lst):
	for i in range(1, len(lst)): #first element is already sorted
		current = lst[i]
		j = i-1 #since it starts at index 1, subtracting for the first one
		#wont result in an error
		while j >= 0 and current < lst[j]:
			lst[j+1] = lst[j]#so instead of switch them each time, I decided that was
			#inefficient, so now they all move to their new positions, rather than
			#switching them each time
			j -= 1
		lst[j+1] = current #reset the variable to the next time to check for,
		#essentially puts items in the "already sorted" bin
	return lst


def main():
	x=np.random.rand(20000)
	insertionSort(x)

if __name__ == "__main__":
	main()






