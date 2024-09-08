"""
Unit: Algorithms Analysis
Goals: 
	1) Develop a language for analyzing and comparing the efficiency
		of different algorithms (time complexity and space complexity)
	2) Learn fundamental algorithms in CS
	3) Improve our programming style (specifically imperative programming)
	

Write a function called search that takes two parameters,
a list and a target item
The function should search for the target item in the list 
if it is found return its index, return its index,
if its not found, return False
"""

def search(list1,target):
	for i in range(len(list1)): #loop through indices 
		if list1[i] == target:
			return i 
	return False #looped through without finding anything 

"""

Each time through the loop we need to: 
	-assigns i to a new value 
	-load value from memory 
	-compare two items (check equality)
Afterwards
	return something 

If we need to pass through the loop N times
how many operations do we do?
approximately 3*N + 1 -- LINEAR 

How many times will the loop run? 
At most, the length of the list 
At least once (if target is first)
WORST CASE SCENARIO - target is last or not present 
	-> the length of the list  (O(n))
BEST CASE SCENARIO - if the target is first 
	-> loop runs once 
AVERAGE CASE - item is roughly in the middle
	-> ~length/2

We care about how the runtime GROWS as the problem gets bigger
Thus example grows linearly as the list gets longer 

BIG-O NOTATION:
N is the "size" of the input
If the runtime is a linear function of N, we say that 
the runtime (aka time complexity) is 
O(N) "Oh of N" / "big-oh of N"

If the runtime is a quadratic function of N, the runtime is 
O(N^2) "Oh of N squared"

Rule for figuring out the big-O notation
	- Ignore all but the fastest growing term 
	- Ignore all coefficients/constant factors 

Examples:
f(n) = 2n^2 + 15n + 107
f(n) = O(n^2)

g(n) = .5n + ONE BILLION
g(n) = O(N)

h(n) = 100n^3 + 2^n
h(n) = O(2^n) "exponential"

w(n) = 503
w(n) = O(1) "constant"

"""

def example(lst):
	for i in range(len(lst)):
		for j in range(len(lst)):
			if lst[i] == lst[j]:
				print("Hello")
#if the list is length N, inner loop runs N^2 times 
#O(N^2)
	
"""
Analyze the run time of the function

How long does it take the function to run 
	How to measure this?
		In Seconds? 
		different on different systems
		different even on the same machine (other processes running )
	-lines of code? 
		-how much stuff the computer has to do 
		-different lines take different amount of time 
	-number of operations on your processor? 
	-

"""
def ex2(lst):
	for item in lst:
		print(lst.index(item)) #.index is O(N)
	#O(N^2)

#main function will call other functions and organize the program
def main():
	lis = [1,2,3,4,5,6,7,8,9]
	print(search(lis,2))

#call main function
#if you are running the file, call main
#if you are importing, don't call main
if __name__ == "__main__":
	main()
