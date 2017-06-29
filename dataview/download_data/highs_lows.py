import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)
fig = plt.figure(dpi=128, figsize=(8, 4))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title('Daily high temperatures july 2014', fontsize=24)
plt.xlabel('', fontsize=10)
fig.autofmt_xdate()
plt.ylabel('Tempertrues (F)', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()
