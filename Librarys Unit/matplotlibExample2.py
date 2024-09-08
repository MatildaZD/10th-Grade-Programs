import matplotlib.pyplot as plt 

xs = [0,1,2,3,4,5]
ys = [x**2 for x in xs] #list comprehension

print(ys)

plt.scatter(xs, ys)
plt.show()