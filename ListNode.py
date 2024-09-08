"""
LIST NODE

so far all of the data structures weve implemented have been built on lists 
Python Lists are implemented as dynamic arrays 

Arrays are stored as sequences of items in a contiguous block of memory

[5,10,15,20] -> these items will be next to eachother in memory

This allows constant time random acess 
The adress of any index can be computed in a single step as 
(addess of index) = (address of an array start) + item_size * index

This is not how lists work in most programming languages
In other languages the term "list" refers to a linked list
which are totally different way of storing sequential data 

List Node:

Cotains two fields:
1)data - whatever is being stored in the list
2)link - momeory address of the next node in the chain

Linked List:
-A sequential Data Structure made up of itmes stored in list nodes
-The ordering of the sequence is determined entirely by the links between the nodes

"""

class ListNode:
	def __init__(self, value):
		self.data = value #initialize data field to store value passed in
		self.link = None 
		#initialize with no link since we dont know where it will point
		#eventually this will be set to another ListNode Object
	
	def __str__(self):
		if self.link == None:
			str(self.data)
		return str(self.data) + "->" + str(self.link)

	def setNext(self,node):
		self.link = node

	def setData(self,value):
		#update data stored in this node 
		self.data = value

	#return the next node in the chain
	def getNext(self):
		return self.link

	def getData(self):
		return self.data

	



def main():
	nodeA = ListNode("Matilda")
	nodeB = ListNode("David")

	NodeA.setNext(nodeB)

	#create a new node and link it after Node B 
	nodeB.setNext(ListNode("Yana"))
	print(NodeA)

	#add daniel to this chain BETWEEN David and Yana 
	nodeC = ListNode("Daniel")
	nodeC.setNext(nodeB.getNext())
	nodeB.setNext(nodeC)

if __name__ == "__main__":
	main()






