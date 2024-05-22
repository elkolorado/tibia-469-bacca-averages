import matplotlib.pyplot as plt

def plot_digit_occurrence(text):
    digit_counts = [text.count(str(i)) for i in range(10)]

    plt.figure()
    plt.bar(range(10), digit_counts)
    plt.xlabel('Digit')
    plt.ylabel('Occurrence')
    plt.title('Digit Occurrence')
    plt.xticks(range(10))
    return plt


if __name__ == '__main__':
    text = input('Enter some text: ')
    plot_digit_occurrence(text)