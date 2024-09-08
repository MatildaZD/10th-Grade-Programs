"""
The stack data structure
This Data structure is organized as an ordered stack/pile of items in
which we add or remove only from the top 
	The available operations:
	1. Push 
		adds item to top
	2. Pop
		removes and returns the item at the top 
	3. Peek
		returns the top item but doesnt take it off
	4. isEmpty()
		returns True if the stack is empty 

-There is no way to access items that are not on top 
-Stacks operate using a LIFO ("last in, first out") rule

Examples?
	- crowded elevator
	- jar of cookies
	- the back button on a browser
	- the undo function on a text editor
	- Recursion/function calls 

Implement the stack DS
	-probably using a list as the internal implementation 
"""
class Stack:

	def __init__(self):
		self.stack = []

	def __str__(self):
		return str(self.stack)

	def push(self,added):
		self.stack.append(added)

	def pop(self): 
		return self.stack.pop(-1)

	def peek(self):
		return self.stack[-1]

	def isEmpty(self):
		if self.stack == []:
			return True
		else:
			return False


def main():
	s = Stack()
	s.push(6)
	s.push(2)
	s.push(1)
	print(s.__str__())
	s.pop()
	print(s.peek())
	print(s.isEmpty())


if __name__ == "__main__":
	main()






