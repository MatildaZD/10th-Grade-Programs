
"""
The Hailstone function is defined as follows:

     If x is even, H(x) = x/2

     If x is odd, H(x) = 3*x + 1

   This is not yet recursive. However, interesting things happen 
   when we use it to define a sequence. We start with any number, 
   and each subsequent number in the sequence is created by applying 
   H to the number before. For example, if we start with 7, we get the 
   sequence.

7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.

Empirically, it has been observed that all sequences 
eventually reach 1 (and then get stuck in a loop). However, it has 
never been proven mathematically that this will happen for all numbers.
"""

#1
def hailstone(n):
	print(n)
	if n==1: #base case
		return
	#recursive step
	elif n%2 == 0: #if even, do n/2 
		return hailstone(n//2)
	else: #if odd, do 3n+1
		return hailstone(3*n + 1)
		
"""
Write a recursive function that takes a string, and 
returns a version of the string with all the spaces removed.
"""
#2
def removeSpace(string):
	if len(string) == 0:
		return string #if there is nothing in the input just return empty
	elif string[-1] == " ": #if the last item is a space, remove it
		return removeSpace(string[:-1])
	else: #if it is not a space, remove the last item, but then add it back after
	#this ensures it checks each item to until there are 0 characters 
		return removeSpace(string[:-1]) + string[-1]

"""
Write a recursive version of findMin, a function that 
takes a list and returns the smallest number in the list.
"""
#3
def findMin(lis):
	if lis == []:
		return "empty" #base case
	elif len(lis) == 1: #if the length is 1, just return the value
		return lis[0]
	elif lis[0] <= lis[-1]: #if first item is less than last item
	#recurse through without the last item
		return findMin(lis[:-1])
		#otherwise remove the first item 
	elif lis[0] >= lis[-1]: 
		return findMin(lis[1:])

#list1 = [3,6,3,2,-333,6,8,5,4,3,45,-78,-333,2,1,6,-1]
#print(findMin(list1))

"""
Write a recursive function that takes a string and a 
character and returns the number of times that character 
appears in the string.
"""
#4
def numAppear(string, n, x): #not sure if this is cheating
#but I decided to use another input as a counter so I would not have to
#alter n
	if len(string) == 0:
		return x
	elif string[-1] == n:
		return numAppear(string[:-1],n, x+1) #adds one to the counter
		#if the last character is the character you are looking for
	else: 
		return numAppear(string[:-1],n, x) #otherwise just pass by it
		#return len(string)

print(numAppear("lllhello llllllauren", "l", 0)) #8
#somewhat odd way of doing it with a third parameter, but it works
#not sure how effective it is


"""
Write a recursive function that takes an integer n, and prints out the 
first n rows of Pascal's triangle.
"""
#5
def pascal(n):
	if n == 0:
		return [] #0th row = []
	elif n == 1:
		return[1] #1st row = [1]
	else:
		new = [1] #makes a new row
		last = pascal(n-1) #recursive call
		print(last)
		for i in range(len(last)-1):
			new.append(last[i]+last[i+1]) #append i in list and i+1 in list 
			#to create the effect of pascals triangle 
		new.append(1)#appends 1 to the end
	return new

print(pascal(6))

			

"""
Write a function that determines whether a number is prime
"""
#8
def prime(n,n2):
	if n%n2 == 0: #until this = 0, its a prime number
		return False
	elif n2>2: #until n2>2 (not sure why it is 2 and not 1) keep calling the function 
		return prime(n,n2-1)
	else:
		return True #if there are no n%n2 = 0, its prime 

print(prime(173,172))








