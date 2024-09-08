"""
Recursive Reasoning
1) What is the base case?
2)What is the recursive step?

Base case for sorting:
 Single item or empty list --> already sorted

How do we split up the problem? 
	-everything but the first item
		-Recursive insertion sort
	-split the length in half
		-Call function on each half to sort


[2,3,7,1,8,5,4,6]
left		right
[2,3,7,1]	[8,5,4,6]

[1,2,3,7]	[4,5,6,8]

-Need to combine the two sorted halves, to create a full, sorted list
"MERGE"

MERGESORT(lst):

	if len(lst) <= 1:
		return lst
	else: 
		MERGESORT(lefthalf)
		MERGESORT(righthalf)
		return MERGE(left + right)


"""
"""
def MERGESORT(lst):

	if len(lst) <= 1:
		return lst
	else: 
		MERGESORT(0:len(lst)/2)
		MERGESORT(len(lst)/2:-1)
		return merge(left + right)
"""

def merge(lst1,lst2):
	new = []
	counter1=0
	counter2=0 
	while len(new) < len(lst1)+len(lst2): #if the length of the new list
	#gets bigger than the length of the other lists
	#leave the loop 
		if lst1[counter1]>=lst2[counter2]:
			new.append(lst2[counter2])
			if lst2[-1] in new:
				new.append(lst1[counter1])
			else:
				counter2+=1
			
			print("counter2 = ", counter2)
		else:
			new.append(lst1[counter1])
			if lst1[-1] in new:
				new.append(lst2[counter2])
			else:
				counter1+=1
			
			print("counter1 = ", counter1)
					
	return new


#for the purpose of the recursive sort, this technically works. You just
#have to make sure list 1 is the longer list. 
lst1 = [4,5,6,8,10]
lst2 = [1,2,3,9]
print(merge(lst1,lst2))









