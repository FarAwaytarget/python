# coding = utf-8
from matplotlib import pyplot as plt
a = [1,2,3,4,5,6]
b = [2,4,6,8,10,12]
plt.plot(b,a, c='red')
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()