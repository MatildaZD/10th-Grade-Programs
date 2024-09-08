#create a FOIL calculator

import numpy as np
import random 

def createValues():
	chance = random.randint(1,5)
	if chance <= 3: 
		a = random.randint(1,15)
		b = random.randint(1,15)
		c=1
		d=1
	else: 
		a = random.randint(1,15)
		b = random.randint(1,15)
		c = random.randint(2,4)
		d = random.randint(2,4)
	values = [a,b,c,d]
	return values

def createPoly(lst):
	p1 = np.poly1d([lst[2], lst[0]])  
	p2 = np.poly1d([lst[3], lst[1]])
	mul = np.polymul(p2, p1) 
	return mul  

values = createValues()

def checkAnswer(a,b):
	correct = "Correct!"
	incorrect = "Wrong!"
	if a == values[0]/values[2] or a == values[1]/values[3] and b == values[0]/values[2] or b == values[1]/values[3]:
		return correct 
	else: 
		return incorrect

	


print("Find the roots of this quadratic equation!:\n", createPoly(values))
a = int(input("Enter first root:"))
b = int(input("Enter second root:"))
print(checkAnswer(a,b))



