import matplotlib.pyplot as plt

x_value = list(range(1, 5001))
y_value = [pow(x, 3) for x in x_value]
plt.scatter(x_value, y_value, c=y_value,
             s=40)
# set title name
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of value', fontsize=14)

plt.tick_params(axis='both', which='major', size=5)
plt.show()
