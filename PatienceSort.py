import numpy as np

def patienceSort(lst):
	piles = []
	while lst != []: #until the list is empty because you are popping items off the list
		val = lst.pop(0) #set the variable val to the first item in lst, then
		#remove that item from the list so it does not set it to the same number again 
		checker = False
		for i in piles: #first time through, nothing will happen
			#checks every pile already created 
			if i[-1] > val: #if the first value 
				i.append(val) #insert the value at the list 
				checker = True #make sure you dont create a new list at the end
				break #breaks out of the loop if the value has been placed
		if checker == False: #the first time through it will make the first stack
			#checker is set to true if there is a value for the number
			#so it will not create a new pile if so
			i = [val] #make value into new list
			piles.append(i) #add this new list to the pile 

	#this loop will repeat for every item in list 
		
	sortedlst = []
	while piles != []:
		smallestval = float('inf') #set smallest value to initially always be higher than
		#p[-1]
		smallestpile = None #set to none so it doesnt actually have any value
		for p in piles: 
			if p != [] and p[-1] < smallestval: #this step will repeat
			#until smallest value found and smallest pile is found
				smallestpile = p
				smallestval = p[-1]
		sortedlst.append(smallestval) #once smallest val is found it is then appeneded
		smallestpile.pop(-1) #then popped off the smallest pile
		if not smallestpile: #short way of saying if its empty, 
		#and if it is, then remove the pile from the piles list.
			piles.remove(smallestpile)
			#everything is then repeated until there are 0 piles left. 
	return sortedlst

#if you want to use a numpy array on this algorithm, you have to
#reset it to a list, so once you initialize it, just set it
#lst = list(lst)		
	


def main():
	lst = [9,4,5,2,1,7,12,10,13,3,6]
	lst2 = np.random.random(10000)
	lst3 = np.arange(1000)
	lst4 = np.arange(1000,0,-1)
	#100,000 random = 7.2 seconds
	#10,000 random = 0.482 seconds
	lst2 = list(lst2)
	lst3 = list(lst3)
	lst4 = list(lst4)
	print(patienceSort(lst3))

if __name__ == "__main__":
	main()