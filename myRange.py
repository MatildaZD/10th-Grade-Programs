#rewriting of the range object
class myRange:
	#initialize a range object
	def __init__(self,start,stop,step):
		self.start = start
		self.stop = stop
		self.step = step
	
	#this iter method initializes the current value 
	#and returns itself as the iter 
	def __iter__(self):
		self.current = self.start
		return self

	#return the next value and 
	#update the current value until stop
	#is reached
	def __next__(self):
		value = self.current
		self.current += self.step
		#positive step size counts up 
		if self.step >= 0 and value <= self.stop:
			return value
		#negative step size counts down 
		elif self.step < 0 and value >= self.stop:
			return value
		else:
			raise StopIteration


def main():
	for i in myRange(1,15,3):
		print(i)



if __name__ == "__main__":
	main()







