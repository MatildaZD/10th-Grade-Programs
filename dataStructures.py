"""
DATA STRUCTURES

The way we store and organize data can make huge a difference on how 
efficient code will be 

A data structure is a system of storing, organizing, and 
manipulating data in a programming language 

Some data structures that we have used before:
	-Python List
	-Array (numpy)
	-Dictionary
	-Tuple
	-String

Essential Questions
1. How is the data organized logically? 
	-Python List: Indexed (each item has a specified position), an ordered 
	sequence, data can be of multiple types. 
	-Array: Fixed size, indexed, single data type, 
	-Dictionary: unordered set of key-value pairs, Each key is associted with a value  
2. What operations are availible to us to access and manipulate the data?
	Lists:
		-Append, pop, remove, insert
		-acess by index, resassign an individual index (random access)
		-.sort(), 
		-iternate through a list
		-get the length
		-slice
		-find the min or max
	Dictionaries:
		-Add a key, value pair
		-change the value for a key 
		-itterate through keys and/or vals
		-lookup a key 
	Tuple:
		-immutable
		-but can still iterate or access by index
3. How can these operations be implemented and how efficient are they?
	Lists:
		Python Lists are implemented as 'dynamic arrays'
		The list is really an array, that is resized when necessary
		Appending to a list is on average O(1) but sometimes the whole
		list needs to be copied when we run out of space 
		-pop(0) --> requires each item to be moved over to the left (O(n))
		-pop() --> O(1) 
	Dictionaries: 
		dictionaries have O(1) lookup of keys
		-> built on top of hash tables
"""









