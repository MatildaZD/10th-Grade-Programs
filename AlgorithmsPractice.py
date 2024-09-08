"""
1) Write a function safeGet, which takes a list and an 
index as parameters. If the index is a valid index, 
it should return the item at that index in the list. 
If not, it should return -1. You should never get an 
index out of range error.

2) Write a function factorial, that takes an integer 
parameter and computes and returns the factorial 
of that integer. factorial 

3)Write a function anyFactors, that takes a list as a parameter.
It should return True if ANY number in the list is a factor 
of any OTHER number, and False otherwise. 
Hint: a % b returns the remainer you get if 
you divide a / b.  a % b == 0 when b is a factor of a.
"""


#1: 
def safeGet(lst,p):
	try:
  		print(lst[p])
	except:
  		print(-1)

#Big O Notation is O(1) because all it has to do it run the list ones
#and find the value, the worst case scenario is if the item
#is not within the list and it just ran through the whole list
#and did not find anything. 


#2:
def factorial(num):
	count = 1

	for i in range(1,num+1):
		count = count * i
	return count

#Big O notation for this I believe would also be O(n)
#because it is lineraly expanding. Say you input 7, it would just
#have to run the loop one less time than if you inputted 8. 

#3:
def anyFactors(lst): 
	for i in range(len(lst)):
		for j in lst[:i] + lst[i+1:]: 
			if lst[i] % j == 0:
				return True

	return False 
#the big O notation here I believe would be O(n^2). I am not
#sure if the if statement would make it cubed, but I think
#that since is has to run through the list for each item in
#the list, it will be O(n^2)


