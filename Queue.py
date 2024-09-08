"""
The Queue Data Structure
A queue is an ordered sequence in which items are added
the the "back" of the queue and removed form the "front"

A queue follows the rule of FIFO ("First-in, first-out")

A queue has the following operations:
	1) enqueue() -  add an item to the back of the queue

	2) dequeue() - remove and return item at the front of the queue

	3) peek() - return the item at the front

	4) isEmpty() 

Examples:
	- Online shopping , waiting for limited supply
	- Used in web servers to handle multiple requests
	- used in operating systems to assign processor time

"""

#Implement a queue data structure by writing a class.

#Challenge: Implement all 4 operations in O(1) if possible


# class Queue:
# 	def __init__(self):
# 		self.q = [] #empty queue

# 	def __str__(self):
# 		return str(self.q)

# 	#O(1)
# 	def enqueue(self, item):
# 		#the front of the queue is the beginning on the list
# 		self.q.append(item)

# 	#O(N) b/c we pop from beginning of a list
# 	def dequeue(self):
# 		return self.q.pop(0) #removes and returns the item at the front of the queue
# 								#which is the start of the list

# 	#O(1)
# 	def peek(self):
# 		return self.q[0]

# 	#O(1)
# 	def isEmpty(self):
# 		return len(self.q) == 0



class Queue:
	def __init__(self):
		self.q = [] #empty queue
		self.front = 0 #index of the item at the front of the queue

	def __str__(self):
		return str(self.q[self.front:]) #slice from front to end of list

	#O(1)
	def enqueue(self, item):
		#the front of the queue is the beginning on the list
		self.q.append(item)

	#O(1)* on average (amortized analysis)
	def dequeue(self):


		#if more than half the storage is wasted
		#This operation is O(n)
		if self.front >= len(self.q) // 2:
			item = self.q[self.front] #save item to return
			self.q = self.q[self.front+1:] #remove item and all wasted space
			self.front = 0 #reset front of queue to index 0
			return item
		else:
			self.front += 1 
			return self.q[self.front - 1] #returns the item that was at the front of the queue

	#O(1)
	def peek(self):
		return self.q[self.front]#return the item at the front of the queue

	#O(1)
	def isEmpty(self):
		return len(self.q) == self.front

"""
Storage Issue:
Imagine alternating between enqueuing and dequeuing an item 1 million times

the Queue's internal list will keep growing
"""


"""
Alternate strategy:
Circular Buffer
data "wraps around" back to the start of the list
"""


