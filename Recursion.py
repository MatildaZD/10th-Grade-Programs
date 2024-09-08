def hanoi(n, source, intermediate, destination):
	if n == 1: #Base Case
		print("move disc " + str(n) + " from " + source + " to " + destination + ".")
	else: # Recursive Step
		hanoi(n-1,source,destination, intermediate)
		print("move disc " + str(n) + " from " + source + " to " + destination + ".")
		hanoi(n-1,intermediate,source, destination)



hanoi(4, "pile 1", "pile 2", "pile 3")


lst = [3,15,2,13,8,4]
#write a function to compute the sum of the list 

"""
Recursive thinking
-What is the size of the problem?
	Length of the list
-What is the simplest version of the problem? (Base Case)
	an empty list
	sum is zero
-Recursive step
	list 1 item shoter (everything but the first item)
	assume the fucntion works to find the sum of
		everything bt te first item
	add the first number to that sum
"""

def listSum(l): 
	if l == []: #base case empty list
		return 0 #sum of an empty list is 0 
	else:
		#list[1:] slice of everything but index 0 
		#first number + sum of rest of list 
		return l[0] + listSum(l[1:])
"""
[3,15,2,13,8,4]

listSum([3,15,2,13,8,4])
1. 3 + listSum([15,2,13,8,4])
2. 15 + listSum([2,13,8,4])
3. 2 + listSum([13,8,4])
4. 13 + listSum([8,4])
5. 8 + listSum([4])
6. 4 + listSum([])
7. 4 + 0 = 4
8. 8 + 4 + 13 + 2 + 15 + 3 = 44






Fibonachi Sequence

1,1,2,3,5,8,13,21...

"""
#return the nth number in the sequence 
def fibo(n):
	#two base cases
	if n== 1 or n==2:
		return 1
	else: #recursive step 
		return fibo(n-1) + fibo(n-2)







