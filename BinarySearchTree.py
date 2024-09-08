"""
Binary Search Tree
Binary tree where for all nodes every value in the left subtree is less
than or equal to every value 

"""
from TreeNode import TreeNode 

class BST:

	def __init__(self):
		self.root = None

	def __str__(self):
		return str(self.root)

	#add a new value to the binary search tree and maintain the properties

	def add(self,value):
		if self.root is None:
			#set root to a new node
			self.root = TreeNode(value)
			return 
		current = self.root
		while True:
			if value > current.getData(): #if value is greater than the current current
				if current.getRight() is None: #if the value is not already there
				#set the value
					current.setRight(TreeNode(value)) 
					break
				else: 
					current = current.getRight() #otherwise set it to the next value and repeat
			else: 
				if current.getLeft() is None: 
					current.setLeft(TreeNode(value))
					break
				else: current = current.getLeft() 

	

	#return true if the value is present 
	#return false if its not
	def search(self,target):
		current = self.root
		while current is not None: #while loop until we find none
			if target == current.getData():
				return True #if we find the data within the loop we return True
			elif target < current.getData():
				current = current.getLeft() #will keep resetting until it is found
			else: 
				current = current.getRight()

		return False #the loop will be exited if it is not found and then we just return False 

def main():
	tree = BST()
	tree.add(5)
	tree.add(6)
	tree.add(4)
	tree.add(16)
	tree.add(13)

	print(tree)
	#print(tree.search(7))

if __name__ == "__main__":
	main()




