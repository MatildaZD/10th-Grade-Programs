from ListNode import ListNode
class LinkedList:

	#initialize fields that we need to manage
	#a linked list
	def __init__(self):
		#a pointer to the first node in the list
		self.head = None
		self.length = 0
	def __str__(self):
		return str(self.head)
	"""
	Methods that begin and end with double
	Underscores are called "dunder" methods 

	Implementing __len__ makes us able to call len on objects 
	of the linked list class 
	"""
	def __len__(self):
		return self.length

	def __getitem__(self,index):
		return self.get(index)

	def __setitem__(self, index, value):
		self.set(index,value)

	def __iter__(self):
		#variable to store the state of the iterator 
		self.cNode = self.head
		return self

	#return the next value in the list and update self.cNode 
	#raise StopIteration if we are done
	def __next__(self):
		#if none we are at the end 
		if self.cNode == None:
			raise StopIteration
		value = self.cNode.getData()
		self.cNode = self.cNode.getNext() #update current node
		return value #return current data item 

	#add a node with the given data item 
	#to the front of the linked list 
	def addFirst(self,item):
		NewNode = ListNode(item)
		#connect new node to the node 
		#that used to be in front of the list
		NewNode.setNext(self.head)
		#reassign new node as head
		self.head = NewNode
		self.length += 1

	#in a python list, the runtime of accessing an item by index
	#(lst[5]) was O(1) - constant time random access 

	#In Linked Lists, accessing an item by index,
	#is O(N) - linear 
	#linked lists can be efficiently iterated through but only if we are visiting the nodes
	#sequentially
	#sequential access vs random access 

	def popFirst(self):
		if self.head != None:
			temp = self.head.getData()
			self.head = self.head.getNext()
			self.length -= 1
			return temp
		else:
			raise ValueError("Empty List")

	def get(self, index):
		if index < 0 or index >= self.length:
			raise ValueError("Index out of bounds")
		count = 0
		current = self.head
		while count < index:
			current = current.getNext()
			count += 1
		return current.getData() 

	def set(self, new, index):
		if index < 0 or index >= self.length:
			raise ValueError("Index out of bounds")
		count = 0
		current = self.head
		while count < index:
			current = current.getNext()
			count += 1
		current.setData(new)
		
	def insert(self, item, index):
		if index < 0 or index > self.length:
			raise ValueError("Index out of bounds")
		if index == 0:
			self.addFirst(item)
		else: 
			count = 0
			current = self.head
			while count < index - 1:
				current = current.getNext()
				count += 1
		NewNode = ListNode(item)
		NewNode.setNext(current.getNext())
		current.setNext(NewNode)
		self.length += 1
	
	def pop(self, index):
		if index < 0 or index >= self.length:
			raise ValueError("Index out of bounds")
		count = 0 
		count2 = 0
		current = self.head
		current2 = self.head
		while count < index: #gets item to be popped
			current = current.getNext()
			count += 1
		while count2 < index-1: #gets item before item to be popped
			current2 = current2.getNext()
			count2 += 1
		current2.setNext(current.getNext())
		if index == 0: #in case its at the front (popFirst code)
			temp = self.head.getData()
			self.head = self.head.getNext()
			self.length -= 1
			return temp
		self.length -= 1
		return current.getData()
			
	#find the node containing the target value if present
	#return false if not present
	#otherwise return the index of the target value 
	def search(self, target): 
		index = 0 
		current = self.head
		#currently looking at this node

		while index < self.length:
			if current.getData() == target:
				return index
			index += 1
			#go to next node 
			current = current.getNext()
		return False 

def main():
	#create an empty linked list 
	ll = LinkedList()
	ll.addFirst("Daniel")
	ll.addFirst("Lauren")
	ll.addFirst("Rohan")
	ll.addFirst("Ishan")

	for name in ll:
		print(name)
	
if __name__ == "__main__":
	main()










