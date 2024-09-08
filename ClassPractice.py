class SortedList:

	def __init__(self, lst1):
		self.lst = lst1

	def search(self, target): #binary search code
		start = 0
		end = len(self.lst) - 1
		while start <= end:
			mid = (start + end) // 2
			if target < self.lst[mid]:
				end = mid - 1
			elif target > self.lst[mid]:
				start = mid + 1
			else:
				return mid
		return False

	def findMax(self):
	  if len(self.lst)==0:
	    return False
	  return self.lst[-1]

	def findMin(self):
	  if len(self.lst)==0: 
	    return False
	  return self.lst[0] #use last item because it is already sorted 

	def findMedian(self): 
	  if len(self.lst) % 2 == 0: #make sure to know what to do when the list is even length
	    median = (self.lst[len(self.lst) //2] + self.lst[len(self.lst)//2 - 1]) / 2
	    return median
	  return self.lst[len(self.lst) // 2]

	def insert(self, item):
	  def search(self, target): #use a variant on the search function to find the place to insert the value 
	    start = 0
	    end = len(self) - 1
	    while start <= end:
	      mid = (start + end) // 2
	      if target < self[mid]:
	        end = mid - 1
	      elif target > self[mid]:
	        start = mid + 1
	      else:
	        return mid
	    return start
	  index = search(self.lst, item)
	  self.lst.insert(index, item)
	  
	def remove(self, target):
	  index = self.search(target) #use the search function to find the item and then remove that specific item 
	  if (index==False):
	    return False
	  self.lst.pop(index)

def main():
	lst = SortedList([2,3,4,5,7,9,11,15,21])
	
	print(lst.findMax())
	print(lst.findMedian())
	lst.insert(10)
	print(lst.search(10))
	lst.remove(10)
	print(lst.search(10))


if __name__ == "__main__":
	main()