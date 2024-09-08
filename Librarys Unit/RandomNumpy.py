import numpy as np 
import matplotlib.pyplot as plt
import math
#create array 
newRandom = np.random.random((10,10)) *50 -37
newRandom = newRandom.astype(np.int)
print(newRandom)

newRandom2 = np.random.random((10000,1))
newRandom2 = np.sqrt(newRandom2)
plt.hist(newRandom2, 1000)
plt.show()

#NEW ANSWER:
#the square roots continually increse, there is sort of a slope of 1 going
#up the graph. 


