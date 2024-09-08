def hanoi(n, source, intermediate, destination):
	if n == 1: #Base Case
		print("move disc " + str(n) + " from " + source + " to " + destination + ".")
	else: # Recursive Step
		hanoi(n-1,source,destination, intermediate)
		print("move disc " + str(n) + " from " + source + " to " + destination + ".")
		hanoi(n-1,intermediate,source, destination)



hanoi(7, "pile 1", "pile 2", "pile 3")