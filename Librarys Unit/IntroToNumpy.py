import numpy as np 
import matplotlib.pyplot as plt
#numpy is based on the array data structure 

"""differences b/w Arrays and Lists:
	- arrays have a fixed size while lists can change size
	- arrays are homogenous, all items are of the same type.
	- numpy arrays comes with a ton of built in methods and functions 
	- computation on arrays is optimized for speed  
"""

#make an 2x2 grid containing all zeros
twobytwo = [[0,0], [0,0]]

#8x8?
eightbyeight = []
for row in range(8):
	rowlist= []
	for col in range(8):
		rowlist.append(0)
	eightbyeight.append(rowlist)

#print(eightbyeight)
#print(eightbyeight[2][0])#print 3rd row, 1st colum

#in numpy:
#create a 2d array of zeros (default: floats )
grid = np.zeros((8,8)) #parameter is a tuple, (rows, columns)
#print(grid)

anotherOne = np.ones((6,3), dtype=np.int) #create an array full of ones 
#print(anotherOne)

#fill array with somethinf
somethingElse = np.full((3,3), 2)
#print(somethingElse)

#indexing - how you acess/modify entries
grid[2,3] = 5
#print(grid[2,3])#print 3rd row, 4th column entry

#random numbers 
randomNums = np.random.random((5,5)) #5x5 array of random floats 
#print(randomNums)
#print(randomNums.shape)#the dimension of the array
#print(randomNums.size)#number of things in the array 

randomNums = randomNums.reshape((25,1))
#print(randomNums)

#multiply each item in an array by 100
randomNums = randomNums * 100 
#print(randomNums)

#BROADCASTING:
#operations are 'broadcast' to all items in the array 
#ie operations apply item by item 

nums = np.arange(0,64,1)#creates an array with numbers 0 to 63 (counting by 1)
nums = nums.reshape((8,8)) 
print(nums)

nums = nums + 10  #adds 10 to all numbers in the array
#print(nums)

#print(nums>30) #broadcasts the condition to all items and returns an array of booleans 

newRandom = np.random.random((8,8)) *64 +10 #makes a random number between 10 and 73
newRandom = newRandom.astype(np.int)
#print(newRandom)
#print(nums > newRandom)

#print(np.square(nums))

factors = np.arange(1,9)#1 dimensional, length 8
#print(factors * nums)

#ADVANCED ARRAY INDEXING
#SLICING
print("\nSlicing")
print(nums[2:7,2])
print(nums[7,1:7])
print(nums[2:5, 2:5]) #slice both rows and columns 

greaterThan30 = nums >30 #array of booleans
#print(nums[greaterThan30]) #give me all the values for which
							#the corresponding boolean is true
print(nums[nums > 30]) #does same thing
print(nums[nums%3 == 0])

print("SETTING SLICE")
nums[nums % 3 == 0] // 3
print(nums)

xVals = np.random.random(20) * 20 - 10
yVals = np.random.random(20) * 20 - 10
condition = yVals >= xVals**2
plt.scatter(xVals[condition], yVals[condition])
plt.scatter(xVals[~condition], yVals[~condition])
plt.show()


#plot the function y = 2 * sin(x) + 1 
#on the interval (-2pi, 2pi)

x = np.arange(-2*np.pi,2*np.pi, 0.1)
y = 2 * np.sin(x) + 1

plt.plot(x,y)
#plt.show()







