"""
1) Try to write a non-recursive implementation of fibo(n) that 
runs in linear (O(n)) time instead of exponential?

Stretch Goal:

2) Can you write a recursive version of the fibonacci 
function that is still O(n)?

"""

#old (bad) function
def fibo(n):
	#two base cases
	if n== 1 or n==2:
		return 1
	else: #recursive step 
		return fibo(n-1) + fibo(n-2)

#linear function
def fibo2(n):
	list1 = [0,1]
	for i in range(n-1):
		new = list1[-1]+list1[-2]
		list1.append(new)
	return list1[-1]

#linear recursion function

series = [1,1]
def fibo3(n):
	
	if n<=len(series): #if n is less that 2 long (which the series begins as)
		#return 1
		return 1
	else:
		holder = fibo3(n-1) + fibo3(n-2)
		#its going to keep going down until it hits 1 and then add all of the numbers
		#together in one step, and appending them each time 
		if n>len(series):#until n is larger than the length of the series
		#it tells the recursion to keep appending the new number until
		#the list is as long as the integer n.
			series.append(holder)
		return series[n-1] #it then returns the final holder it creates
		#not sure if this is allowed. Its a combination of using a list
		#and recursion... Its a bit of a janky solution, def can be improved.

		#This is much faster than the original o^n function
		#I am not really sure why though, it still runs through the recursion twice within
		#itself. I presume it is because of the improved base case
		#I just wanted to combine the two: lists and recursion to see if it would work
		#and it did. 

		#method of saving the values of previously computed results
		#is called "memoization"
		#the method of usuing memoization to solve a problem by storing
		#answers to repeated sub problems is called 
		#dynamic programming

print(fibo3(100))
