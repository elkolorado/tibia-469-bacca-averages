import json
import random
from utils.digit_average import plot_average
from utils.occurence_histogram import plot_digit_occurrence
import matplotlib.pyplot as plt

# Read the JSON file
with open('utils/rand.json') as file:
    data = json.load(file)
    # get the books key


a = plot_average(data['books'])
b = plot_digit_occurrence(''.join(data['books']))



plt.figure()
plt.bar(range(len(data['averages'])), data['averages'])
plt.xlabel('Book no.')
plt.ylabel('Average')
plt.title('Average of digits in random numbers')
plt.xticks(range(len(data['averages'])))
#plot the line 4.5
plt.plot([4.5] * len(data['averages']), 'r--')



# color all the bars are closest to 4.5 +- 0.05
index = [i for i, x in enumerate(data['averages']) if 4.47 <= x <= 4.53]
for i in index:
    plt.bar(i, data['averages'][i], color='b')
    # and print the index of the bars with their average rounded to 2 digits
    for i in index:
        plt.text(i, data['averages'][i], f'{round(data["averages"][i], 2)}', fontsize=9, rotation=45)
# color all the bars are closest to 4.5 +- 0.05
index = [i for i, x in enumerate(data['averages']) if 4.49 <= x <= 4.51]
for i in index:
    plt.bar(i, data['averages'][i], color='r')
    # and print the index of the bars with their average rounded to 2 digits
    for i in index:
        plt.text(i, data['averages'][i], f'{round(data["averages"][i], 2)}', fontsize=9, rotation=45)


plt.show()

