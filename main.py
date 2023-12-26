from matplotlib import pyplot as plt
from random import randint
import numpy as np

n = 10000
flips = [randint(0, 1) for i in range(n + 1)]
cum_sum = []
for i in range(1, len(flips)):
    cum_sum.append(sum(flips[:i]) / len(flips[:i]))


x = np.linspace(0, n, n)
y = np.full_like(x, 0.5)

plt.plot(x, y, color='red')
plt.plot([i for i in range(n)], cum_sum)
plt.ylim(0, 1)
plt.xlim(0, n)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
