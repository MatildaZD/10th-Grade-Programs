import numpy as np
#from FILENAME import FUNCTIONNAME
from MergeSort import mergeSort
from QuickSort import quickSort

def main():
	lst = np.arange(10000)
	lst2 = np.random.random(10000)
	
	quickSort(lst)
	
	#mergeSort(lst)
	#print(lst)

if __name__ == "__main__":
	main()
