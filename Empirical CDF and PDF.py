import numpy as np
import matplotlib.pyplot as plt
from random import random

def f(x):
    return (x**2 - 3*x + 4)/(x**2 + x + 1)

def F_n(x, t):                                                #Эмпирическое распределение
    N = len(x)
    dist = (x < t).astype(int)
    return sum(dist)/N

quan = 10**6;
X = np.random.uniform(-2, 2, quan)
# X = np.random.triangular(-2, 0, 2, quan)
res = np.array(f(X))

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)   # добавление области рисования ax
n, dom, patches = ax.hist(res, bins=80, alpha=0.8)

range_of_values = np.array([F_n(res, elem) for elem in dom])

fig2 = plt.figure(figsize=(12,12))
ax2 = fig2.add_subplot(111)   # добавление области рисования ax
ax2.plot(dom, range_of_values, alpha=0.8)
