import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=5)
# set chart title, and axis add lable
plt.title('Square NUmbers', fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel('Square of value', fontsize =14)
# set scale mark size
plt.tick_params(axis='both', size=4)
plt.show()
