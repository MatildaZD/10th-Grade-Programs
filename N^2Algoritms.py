from InsertionSort import insertionSort
from BubbleSort import bubbleSort
from SelectionSort import selectionSort 
import numpy as np
from numpy import random








def main():
	randomlst = list(np.random.rand(5000))
	sortedlst = np.arange(5000)
	descendinglst = np.arange(5000,0,-1)

	#insertionSort(randomlst) #1.99 seconds
	#insertionSort(sortedlst) #0.38 seconds
	#insertionSort(descendinglst) #8.74 seconds

	#selectionSort(randomlst) #2.16 seconds
	#selectionSort(sortedlst) #0.42 seconds
	#selectionSort(descendinglst) #7.393 seconds

	#bubbleSort(randomlst) #4.19 seconds
	#bubbleSort(sortedlst) #0.66 seconds
	#bubbleSort(descendinglst) #15.49 seconds 



if __name__ == "__main__":
	main()