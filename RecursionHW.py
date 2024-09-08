def factorial(n):
	if n <= 1: #base case
		return 1
	else: #recursive step
		return n * factorial(n-1)


def reverse(lst):
	if lst == [] or len(lst) == 1: #base case: if there is an empty list or a list with
	#one item, just return the list by itself
		return lst
	else: #recursive step 
		return reverse(lst[1:]) + [lst[0]] #the extra brackets turns it into a list
		#so it can concatenate.  


def palindromeCheck(string):
	if len(string) < 1: #base case
		return True
	else:
		if string[0] == string[-1]: #if the last two letters match then input
			#the word minus the two at the beginning and end until there is less than 1
			return palindromeCheck(string[1:-1])
		else: 
			return False
	
		







