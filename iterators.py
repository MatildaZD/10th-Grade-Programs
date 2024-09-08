
#lst = ['a', 'b', 'c', 'd']
#iterate through items in collections 
#for item in lst:
#	print(item)

"""
It would be nice if you could use this for-in syntax in classes that we write 

we actually can if we implement special "dunder" methods

Iterators are objects that implement the __next__()
dunder method. They need to somehow maintain the current
state. The __next__() method updates that to the next item
and returns its value

Objects that can be iterated through are called iterable 
and they must implement the dunder method __iter__() which
returns an iterator for that object 

Often the iterable class (has an __iter__ method) will actually
be the same class as its iterator (which has a __next__ method)
"""
class Counter:

	def __init__(self, number):
		self.max = number

	def __iter__(self):
		return CounterIterator(self.max)

class CounterIterator:
	def __init__(self, max):
		self.max = max
		self.value = 1 #keeps track of current value 

	#update value and return value
	def __next__(self):
		self.value += 1
		if self.value <= self.max:
			return self.value 
		else:
			raise StopIteration 


def main():
	counter = Counter(10)
	iterator = counter.__iter__()

	while True:
		try:
			print(iterator.__next__())
		except:
			break

	#when a language has nicer syntax that covers 
	#up something messier than whats really going on
	#its called syntactic sugar
	for c in counter(10):
		print(c)

if __name__ == "__main__":
	main()




