"""
In CS, Tree refers to a non linear, connection based
branched structure of nodes 

(Typically each node stores data)

Key Terms:
-Roots
-Child
-Parent 
-Siblings
-Leaves
-Interior Nodes
-Branching Factor 
-Subtree 
	--> a subtree of a node is a tree consisting of a child
	and all its descendents 

Binary Trees: Branching factor = 2

Applications of trees:
-a tree game states
-indices in binary search (Binary Search Tree)
-Flowchart / decision tree 
	-also used in AI 
-File system on your computer 
	-on UNIX, top level directory is called the root (also known as /)
-Databases
"""

#a tree os built of nodes
#this class implements a tree node for use in 
#binary trees

class TreeNode:

	def __init__(self,value):
		self.data = value 

		#nodes are initialized with no children 
		#left child node
		self.left = None

		#right child node 
		self.right = None 

	def __str__(self):
		if self.left != None or self.right != None:
			#the .format() method replaced {} with values in same order
			return "Node({}, {}, {})".format(self.data,self.left, self.right)
		else:
			return "Leaf {}".format(self.data)



	def getData(self):
		return self.data 

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	#add another node as the left child
	def setLeft(self, node):
		self.left = node 

	#adds another node as the right
	def setRight(self,node):
		self.right = node 


def main():
	node1 = TreeNode(1)
	node2 = TreeNode(2)
	node3 = TreeNode(3)
	node4 = TreeNode(4)
	node5 = TreeNode(5)
	node1.setRight(3)
	node1.setLeft(2)
	node3.setRight(5)
	node3.setLeft(4)

	print(node1)

if __name__ == "__main__":
	main()



