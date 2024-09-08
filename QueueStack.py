from StackNotes import Stack
from Queue import Queue



	

def reverse(q):
	#reverse the items in the input queue
	s = Stack()
	while q.isEmpty() == False:
		temp = q.dequeue()
		s.push(temp)
	while s.isEmpty() == False:
		temp2 = s.pop()
		q.enqueue(temp2)	
	return q

def balance(str1):
	s=Stack()
	s2 = Stack()
	i = 0
	
	while i < len(str1):
		if str1[i] == "(" or str1[i] == "[" or str1[i] == "{":
			s.push(str1[i])
			i += 1
			print(i)
		elif str1[i] == ")" or str1[i] == "]" or str1[i] == "}":
			s2.push(str1[i])
			i += 1
			print(i)
	#ive tried for 45 minutes on this problem and I cannot seem to figure this one out
	#I am dissapointed I couldn't figure out a way to do it but hopefully I will
	#understand tomorrow in class


def palindrome(str1):
	s = Stack()
	length = len(str1)
	mid = length // 2
	i = 0

	while i < mid:
		s.push(str1[i])
		i += 1

	if length % 2 != 0: #make sure to include the middle value  
		i += 1 #if you dont do this, it includes the middle letter and will tell
		#you false for your value because it is looking for another one of a value
		#that doesn't exist
		print(s)

	while i < length:
		temp = s.pop()#takes the last value of the half of the palidrome
		print(str1[i])
		if temp != str1[i]: #compares it to the first of the string
			return False
		i += 1
	return True

def main():
	q = Queue()
	q.enqueue(11)
	q.enqueue(13)
	q.enqueue(15)
	print(q.__str__())
	print(reverse(q))

	print(palindrome("racecar"))

	
if __name__ == "__main__":
	main()