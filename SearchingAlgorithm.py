"""
Psuedocode: 
while there are indices left to check:
	find item in middle position of list 
	compare target to middle item 

	if target > middle item:
		continue our search on the right half
	elif target < middle term
		continue our search on the left half
	else
		we found it!

"""
lst = [0,3,5,7,9,12,15,17,19,20]

def sortSearch(lst,value):
	mini = 0
	mid = 0
	maxi = len(lst) - 1 
	
	while mini <= maxi:
		mid = (mini + maxi) // 2 #floor division, constantly resets mid value
		if value < lst[mid]:
			maxi = mid - 1 
		elif value > lst[mid]:
			mini = mid + 1 #have to do the +1 and -1 one or the function will never stop
		else:
			return mid
	return False


"""
Using a similar method to INSERT items into sorted list (stretch goal )

Psuedocode:
if value is less than midpoint, continue search on left
if value is more than midpint, continue search on right
if value is at midpoint, append it to the left. 

"""

def sortInsert(lst,value):
	mini = 0
	mid = 0
	maxi = len(lst) - 1 
	
	while mini <= maxi:
		mid = (mini + maxi) // 2 
		if value <= lst[mid]:
			maxi = mid - 1 
		elif value >= lst[mid]:
			mini = mid + 1
	if value >= maxi:
		lst.insert(mid+1, value)#I am not sure on other better ways to fix this portion
		#if I try to insert 23, it goes one before the last value so here is the fix
	else: 
		lst.insert(mid, value)
	return lst

print(sortInsert(lst, 23))


	

