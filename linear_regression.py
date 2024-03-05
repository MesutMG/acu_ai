import numpy as np
import matplotlib.pyplot as plt

X = np.arange(0,10)
y = np.array([2, 1, 3, 2, 6, 7,5,8,6,7])

coefficients = np.polyfit(X, y, 1)
line_function = np.poly1d(coefficients)
lrl = line_function(X)

plt.style.use('dark_background')
plt.scatter(X, y)
plt.plot(X,lrl,color="red")
plt.show()


j = np.array([])
for i in range(len(y)):
  sq = (y[i]-lrl[i])**2
  j = np.append(j,sq)
print(np.sum(j)/(2*len(y)))
