# conding=utf-8
from die import Die
import pygal

die = Die()
die2 = Die()
results = []

for roll_num in range(1000):
    result = die.roll() + die2.roll()
    results.append(result)

frequencies = []
label_nums = []
for value in range(1, 13):
    frequency = results.count(value)
    frequencies.append(frequency)
    label_nums.append(value)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = label_nums
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')