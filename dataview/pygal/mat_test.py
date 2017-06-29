from matplotlib import pyplot as plt
from random import randint
class Die(object):
    """ 表示一个骰子的类 """
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """ 返回一个位于1和骰子面数之间的随机值 """
        return randint(1, self.num_sides)

die = Die()
die.roll()
frequencies = []
results = []
for i in range(1000):
    result = die.roll()
    results.append(result)
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_value = [1, 2, 3, 4, 5, 6]
plt.scatter(x_value, frequencies, linewidths=5)
plt.title("Results of rolling one D6 1000 times.")
plt.xlabel(x_value, fontsize=10)
plt.ylabel("Results", fontsize=10)
plt.show()
