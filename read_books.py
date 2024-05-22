import json

# Read the contents of books.txt
with open('utils/books.txt', 'r') as file:
    lines = file.readlines()

# Sort the lines by length
lines.sort(key=len)

# Create a dictionary to store the line lengths and digit occurrences
line_lengths = {}
digit_occurrences = {}
for line in lines:
    line = line.strip()
    line_lengths[line] = len(line)
    for digit in line:
        if digit.isdigit():
            digit_occurrences[digit] = digit_occurrences.get(digit, 0) + 1

# Sort the digit occurrences by the digit
sorted_digit_occurrences = dict(sorted(digit_occurrences.items(), key=lambda x: x[0]))

# Create a sorted array of lengths
sorted_lengths = sorted(line_lengths.values())

# Calculate the total length and total lines
total_length = sum(sorted_lengths)

# Create a dictionary to store the line lengths, digit occurrences, and additional keys
# Strip the lines
stripped_lines = [line.strip() for line in lines]

# Create a dictionary to store the line lengths, digit occurrences, and additional keys
data = {
    'total_length': total_length,
    'digit_occurrences': sorted_digit_occurrences,
    'lengths': sorted_lengths,
    'books': stripped_lines,
    'averages': []  # Add the 'books' key containing the stripped lines
}


# Calculate and add the averages
for line in stripped_lines:
    digits = [int(digit) for digit in line if digit.isdigit()]
    average = sum(digits) / len(digits) if len(digits) > 0 else 0
    data['averages'].append(average)

# Save the data in a nicely formatted JSON file
with open('utils/books.json', 'w') as file:
    json.dump(data, file, indent=4)
