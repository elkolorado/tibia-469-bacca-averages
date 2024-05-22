import random

import matplotlib.pyplot as plt


def plot_average(input):
    results = []

    for _ in range(len(input)):
        digits = []
        digits.extend([int(digit) for digit in str(input[_])])
        average = sum(digits) / len(digits)
        results.append(average)

    plt.figure()
    plt.plot(results)
    plt.xlabel('Iteration')
    plt.ylabel('Average')
    if __name__ == '__main__':
        plt.title('Average of uniformly distributed random numbers')
    else:
        plt.title('Average')
    # trend line
    plt.plot([sum(results) / len(results)] * len(results), 'r--')
    #label trend line with average
    plt.text(0, sum(results) / len(results), f'Average: {sum(results) / len(results)}', fontsize=12)
    return plt


if __name__ == '__main__':
    input = [random.randint(0, 9) for _ in range(1000)]
    plot_average(input)