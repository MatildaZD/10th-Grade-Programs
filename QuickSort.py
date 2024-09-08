"""
Merge Sort
 -split list in half by index
 -hard work takes place in the merge function
 -compares items while recombining halves

Quick Sort
 Another Approach
  -split up the list by *value*

Partition
	-pick one item in the list to be the PIVOT
	-Put all items less than the pivot to the left of the
		pivot
	-put all items greater than the pivot to its right

	After a partition,
		every item to the left of the pivot is less than
		pivot
		the pivot itself is in its final location
		every item to the right is greater than pivot
		(the left and right sides are not necessarily sorted)

quickSort(lst):
	basecase: a list of length 0 or 1 is already sorted
	choose a pivot* and partition
	quickSort the left side
	quickSort the right side

Choice of pivot can matter. For now, choose any item.

Task: Write the partition function

"""

#O(n) time
#(O(1)) space
#takes two indices
#partition iotems between those indices
def partition(lst, start, end):
	pivot = lst[(start+end)//2]

	lst[(start+end)//2], lst[end-1], = lst[end-1], pivot
	
	
	j = start #index of spot to place items less than pivot

	#i is index of item we are comparing to pivot
	for i in range(start, end):
		if lst[i] <= pivot:
			#swap i and j
			lst[j], lst[i] = lst[i], lst[j]
			j += 1 #move j to next spot
	return j - 1 #return final location of pivot


#Runtime (time complexity) of QuickSort
#Partition is O(n)
#we split ~logN times (fewer splits if pivot is closer to median of list)
#QuickSort should be O(nlogn) in the BEST CASE
#WORST CASE: O(n^2)


#Memory complexity: O(1) extra memory

# b/c no copies are made of the list

#outer function only takes one parameter: the list
def quickSort(lst):
	#nested function
	def quickSortHelper(lst, start, end):
		#base case
		if end - start <= 1:
			return

		#returns the location of the pivot
		p = partition(lst, start, end) #call partition on the whole list
	
		quickSortHelper(lst, start, p) #call quickSort on the left (excluding p)
		quickSortHelper(lst, p + 1, end) #call quickSort on the right (excluding p)
		return
	quickSortHelper(lst, 0,len(lst))

"""
Stretch goals:
1) I did spend a long time trying to implement what I read on this wikipedia
article, but with no sucess. It mentioned trying to "choosing the 
median of the first, middle and last element of the partition for 
the pivot. This "median-of-three" rule counters the case of sorted 
(or reverse-sorted) input, and gives a better estimate of the 
optimal pivot (the true median) than selecting any single element, 
when no information about the ordering of the input is known."

In code they said implement this: 

mid := ⌊(lo + hi) / 2⌋
if A[mid] < A[lo]
    swap A[lo] with A[mid]
if A[hi] < A[lo]
    swap A[lo] with A[hi]
if A[mid] < A[hi]
    swap A[mid] with A[hi]
pivot := A[hi]

It puts a median into A[hi] first, then that new value of A[hi] 
is used for a pivot. I could not implement this into my code, however
this article was definitely helpful. 

2)Prove mathematically that the average case (on a random list) of
 quickSort is O(nlogn).

Firs the partition function runs at O(n) time becuase it loops
through the list one time, and then the actual quick sort function
runs O(log n) time for the average case becuase in the average case,
the two items switched will lessen the amount needed sort on that partition by half

not sure if this is fully correct, but this is my interpretation. 

"""